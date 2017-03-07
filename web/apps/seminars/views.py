import logging
import datetime

from flaskcbv.view import TemplateView

from misc.mixins.authed import AuthedMixin, LoginRequiredMixin, AccessMixin

class listView(AuthedMixin, TemplateView):
    template='seminars/list.tpl'

class listCRUDView(AccessMixin, TemplateView):
    template='seminars/crud_list.tpl'
    access_group = 'admin'

