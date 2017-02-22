import logging
import datetime

from flaskcbv.view import TemplateView

from misc.mixins.authed import AuthedMixin

class indexView(AuthedMixin, TemplateView):
    template='index.tpl'


