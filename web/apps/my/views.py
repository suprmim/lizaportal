import logging
import datetime

from flaskcbv.view import TemplateView

from misc.mixins.authed import LoginRequiredMixin

class cabinetView(LoginRequiredMixin, TemplateView):
    template='my/cabinet.tpl'

    def get_context_data(self, **kwargs):
        context = super(cabinetView, self).get_context_data(**kwargs)
        context['user_groups'] = self.access_get_user_groups()
        return context


