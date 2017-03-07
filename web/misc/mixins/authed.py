from flask import url_for
from flaskcbv.response import Response, ResponseRedirect

from auth.auth import authMixin

class AuthedMixin(authMixin):
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


