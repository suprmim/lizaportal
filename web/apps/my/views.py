import logging
import datetime

from flaskcbv.view import TemplateView

from misc.mixins.authed import LoginRequiredMixin

class cabinetView(LoginRequiredMixin, TemplateView):
    template='my/cabinet.tpl'


