from auth.views import authMixin

class AuthedMixin(authMixin):
    def get_context_data(self, **kwargs):
        context = super(AuthedMixin, self).get_context_data(**kwargs)
        self.check_session()
        if hasattr(self.request, 'user') and self.request.user is not None:
            context['user'] = self.request.user
        return context

