import logging
import datetime

from flask import abort, url_for, session as session


from flaskcbv.response import Response, ResponseRedirect
from flaskcbv.view import TemplateView, View
from flaskcbv.view.crud import FormViewMixin

from .forms import LoginForm
from .sessions import Sessions

from utils.db import get_db_session
from models.users.sa_models import Users as UsersModel

db_session = get_db_session(echo=False)


class authMixin(object):
    def check_session(self):
        ## First of all, check user by session:
        session_ = 'session' in session.keys() and session['session'] or None
        uid = Sessions.check(session_)
        if uid is not None:
            user = db_session.query(UsersModel).filter(UsersModel.id==uid).first()
            if user is not None:
                self.request.user = user
                self.request.session = session_
                return True
        return False



class loginView(authMixin, FormViewMixin, TemplateView):
    template='auth/auth.tpl'
    form_class=LoginForm

    def get(self, *args, **kwargs):
        if self.check_session():
            return self.form_valid()
        return super(loginView, self).get(*args, **kwargs)

    def form_valid(self, form=None, **kwargs):
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


