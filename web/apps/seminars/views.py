import logging
import datetime

from flask import url_for
from flaskcbv.view import View, TemplateView
from flaskcbv.view.crud import FormViewMixin
from flaskcbv.response import Response, ResponseRedirect

from misc.mixins.authed import AuthedMixin, LoginRequiredMixin, AccessMixin

from .forms import updateCRUDForm

class listView(AuthedMixin, TemplateView):
    template='seminars/list.tpl'



class listCRUDView(AccessMixin, TemplateView):
    template='seminars/crud_list.tpl'
    access_group = 'admin'



class updateCRUDView(AccessMixin, FormViewMixin, TemplateView):
    template='seminars/crud_update.tpl'
    access_group = 'admin'
    form_class = updateCRUDForm

    def post(self, request, pk=None, **kwargs):
        self.__pk = pk
        return super(updateCRUDView, self).post(request, **kwargs)


    def form_valid(self, form, *args, **kwargs):
        logging.error("DATA: %s" % form.cleaned_data)

        self.__pk = 123
        return ResponseRedirect(url_for('seminars:crud_update', pk=self.__pk))



    def form_invalid(self, form, *args, **kwargs):
        kwargs['form'] = form
        data = self.render_template(*args, **kwargs)
        return Response(data)




class deleteCRUDView(AccessMixin, View):
    access_group = 'admin'


