from flask import url_for, render_template

from flaskcbv.response import Response, ResponseRedirect

from auth.auth import authMixin, accessMixin as authedAccessMixin

class AuthedMixin(authMixin, authedAccessMixin):
    def get_context_data(self, **kwargs):
        context = super(AuthedMixin, self).get_context_data(**kwargs)
        self.check_session()
        if hasattr(self.request, 'user') and self.request.user is not None:
            context['user'] = self.request.user
        return context


class LoginRequiredMixin(AuthedMixin):

    def prepare(self, *args, **kwargs):
        if not self.check_session():
            response = ResponseRedirect(url_for('auth:login'))
            return response.render(headers=self.get_headers())
        return super(LoginRequiredMixin, self).prepare(*args, **kwargs)




class AccessMixin(AuthedMixin):
    access_group = None

    def get_access_group(self):
        return self.access_group

    def prepare(self, *args, **kwargs):
        if not self.check_session():
            response = ResponseRedirect(url_for('auth:login'))
            return response.render(headers=self.get_headers())


        ## Check for access to default group:
        access_group = self.get_access_group()
        if access_group is not None and not self.check_access(access_group):

            ## Render template:
            body = render_template('403.tpl')

            ## Make flaskCBV Response() object:
            response = Response(body)

            ## Make Flask response object with status_code == 403:
            r = response.render(headers=self.get_headers())
            r.status_code = 403
            return r
        
        return super(AccessMixin, self).prepare(*args, **kwargs)
