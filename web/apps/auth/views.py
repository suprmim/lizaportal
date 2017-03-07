import logging
import time, datetime

from flask import abort, url_for, render_template, session as session

from flaskcbv.response import Response, ResponseRedirect
from flaskcbv.view import TemplateView, View
from flaskcbv.view.crud import FormViewMixin

from utils.email.smtp import send_email
from gsettings import settings as global_settings

from .forms import LoginForm, RegisterForm
from .sessions import Sessions
from .auth import authMixin

from utils.db import get_db_session
from models.users.sa_models import Users as UsersModel

db_session = get_db_session(echo=False)


class loginView(authMixin, FormViewMixin, TemplateView):
    template='auth/auth.tpl'
    form_class=LoginForm

    def get(self, *args, **kwargs):
        if self.check_session():
            return self.form_valid()
        return super(loginView, self).get(*args, **kwargs)

    def form_valid(self, form=None, **kwargs):

        ## Create session by self.request.user.id:
        self.authenticate()

        ## User authed but not validated, redirect to validation page:
        if not self.request.user.validated:
	    return ResponseRedirect(url_for('auth:validate'))

        return ResponseRedirect(url_for('index:index'))

    def form_invalid(self, form, *args, **kwargs):
        kwargs['form'] = form
        data = self.render_template(*args, **kwargs)
        return Response(data)



class logoutView(authMixin, View):

    def get(self, *args, **kwargs):
        if self.check_session():
            Sessions().delete(self.request.user.id)

        return ResponseRedirect(url_for('auth:login'))



class confirmationLetterMixin(object):
    token_expire = 3600 ## time for code validation
    template_confirmation_email='auth/register_confirmation.tpl'

    def send_confirmation(self, code):
        self._send_confirmation(
            email=self.request.user.email,
            fio=self.request.user.fio,
            code=code,
            PROJECT_URL=global_settings.PROJECT_URL,
        )

    def _send_confirmation(self, email=None, sms=None, **kwargs):
        if email is None and sms is None:
            return

        ## Sending email confirmation:
        if email is not None:
            body_a = render_template(self.template_confirmation_email, **kwargs).split('\n')
            subject, body = body_a[0], "\n".join(body_a[1:])
            try:
                send_email(email, body, subject=subject)
            except Exception as err:
                logging.error("Can't send confirmation to: %s: %s" % (email, err))

    def generate_confirm_code(self):
        return [time.time()+self.token_expire, Sessions.token_gen(size=8)]




class registerView(confirmationLetterMixin, authMixin, FormViewMixin, TemplateView):
    template='auth/register.tpl'
    form_class=RegisterForm


    def get(self, *args, **kwargs):
        if self.check_session():
            return ResponseRedirect(url_for('index:index'))
        return super(registerView, self).get(*args, **kwargs)

    def form_valid(self, form, **kwargs):

        ## Register user in Database:
        validation_code_a = self.generate_confirm_code()

        user = UsersModel(
            login=form.cleaned_data['username'], passwd=form.cleaned_data['passwd'], 
            email=form.cleaned_data['email'], validated=False, 
            fio=form.cleaned_data['fio'], disabled=False,
            phone=form.cleaned_data['phone'], 
            validation_code=" ".join(map(str, validation_code_a))
        )
        db_session.add(user)
        db_session.commit()

        ## AutoLogout:
        if self.check_session():
            Sessions().delete(self.request.user.id)

        self.request.user = user

        ## AutoLogin: Create session by self.request.user.id:
        self.authenticate()

        ## Send confirmation letter:
        self.send_confirmation(validation_code_a[1])

        return ResponseRedirect(url_for('auth:validate'))

    def form_invalid(self, form, *args, **kwargs):
        kwargs['form'] = form
        data = self.render_template(*args, **kwargs)
        return Response(data)





## ReSend confirmation letter:
class revalidateView(confirmationLetterMixin, authMixin, View):
    def get(self, *args, **kwargs):
        ## Check for auth:
        if not self.check_session():
            return ResponseRedirect(url_for('auth:login'))

        ## Allready validated:
        if self.request.user.validated:
            return ResponseRedirect(url_for('auth:validate'))

        ## Check for prev. token expired:
        if self.request.user.validation_code is not None and self.request.user.validation_code != '':
            expire, utoken = self.request.user.validation_code.split(' ')

            ## If prev. token not expired, got to validation page that show's error about prev. token not expired:
            if int(float(expire)) >= int(time.time()):
                return ResponseRedirect(url_for('auth:validate_confirm', token='tokennotexpired'))


        ## If auth is OK, user is not validated: resend confirmation letter:

        ## Generate new code:
        validation_code_a = self.generate_confirm_code()
        self.request.user.validation_code = " ".join(map(str, validation_code_a))
        db_session.add(self.request.user)
        db_session.commit()
  
        ## Send confirmation letter:
        self.send_confirmation(validation_code_a[1])

        return ResponseRedirect(url_for('auth:validate'))




## Validate account, show validation errors and validation form:
class validateView(authMixin, TemplateView):
    template='auth/validate.tpl'

    def get_context_data(self, **kwargs):
        context = super(validateView, self).get_context_data(**kwargs)
        if hasattr(self, '__error'):
            context['error'] = getattr(self, '__error')
        return context

    def get(self, request, token=None, **kwargs):

        ## Check for auth:
        authed = self.check_session()

        ## If not authed, send to login page:
        if not authed:
            return ResponseRedirect(url_for('auth:login'))

        ## If authed, and allready validated:
        if self.request.user.validated:
            setattr(self, '__error', 'validated')
            return super(validateView, self).get(request, **kwargs)

        ## No validation code is database, show that account is not validated:
        if self.request.user.validation_code is None or self.request.user.validation_code == '':
            setattr(self, '__error', 'notvalidated')
            return super(validateView, self).get(request, **kwargs)

        ## If authed, but no token entered - show our validation form template:
        if token is None:
            return super(validateView, self).get(request, **kwargs)

        ## Tocken is not none, let's check it:
        expire, utoken = self.request.user.validation_code.split(' ')

        ## Tocken allready expired:
        if int(float(expire)) < int(time.time()):
            setattr(self, '__error', 'expired')
            return super(validateView, self).get(request, **kwargs)

        ## If we should show message that token is not expired allready, show it:
        elif token == 'tokennotexpired':
            setattr(self, '__error', 'notexpired')
            return super(validateView, self).get(request, **kwargs)


        ## Wrong token:
        if utoken != token:
            setattr(self, '__error', 'wrong')
            return super(validateView, self).get(request, **kwargs)

        ## Everything is OK, let's validate:
        self.request.user.validated = True
        db_session.add(self.request.user)
        db_session.commit()
        

        ## Go to auth page that will redirect to main:
        return ResponseRedirect(url_for('auth:login'))

