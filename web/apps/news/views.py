import logging
import datetime
import pytz

from sqlalchemy import desc
from sqlalchemy.orm import aliased
from sqlalchemy.sql import func as sa_func
from flask import url_for
from flaskcbv.view import View, TemplateView
from flaskcbv.view.crud import FormViewMixin
from flaskcbv.response import Response, ResponseRedirect

from misc.mixins.authed import AuthedMixin, LoginRequiredMixin, AccessMixin

from utils.db import get_db_session
from models.news.sa_models import News


from misc.tzinfo import myTimeZone


db_session = get_db_session(echo=False)

from .forms import updateCRUDForm


class listView(AuthedMixin, TemplateView):
    template='news/list.tpl'

    def get_context_data(self, **kwargs):
        context = super(listView, self).get_context_data(**kwargs)
        context['news_list'] = db_session.query(News).order_by(desc(News.datebegin)).all()[0:30]
        return context




class detailsView(AuthedMixin, TemplateView):
    template='news/details.tpl'

    def get_context_data(self, **kwargs):
        context = super(detailsView, self).get_context_data(**kwargs)
        context['news'] = db_session.query(News).get(self.__pk)
        return context

    def get(self, request, pk, **kwargs):
        self.__pk  = pk
        return super(detailsView, self).get(request, **kwargs)



class listCRUDView(AccessMixin, TemplateView):
    template='news/crud_list.tpl'
    access_group = 'admin'

    def get_context_data(self, **kwargs):
        context = super(listCRUDView, self).get_context_data(**kwargs)
        context['news_list'] = db_session.query(News).order_by(desc(News.datebegin)).all()
        return context


class updateCRUDView(AccessMixin, FormViewMixin, TemplateView):
    template='news/crud_update.tpl'
    access_group = 'admin'
    form_class = updateCRUDForm

    def get_context_data(self, **kwargs):
        context = super(updateCRUDView, self).get_context_data(**kwargs)
        if hasattr(self, '__obj'):
            context['object'] = getattr(self, '__obj')

            ## No keys in form.data, feel it from object attributes:
            if len(context['form'].data.keys()) == 0:
                for attr in dir(context['object']):
                    context['form'].data[attr] = getattr(context['object'], attr)

        return context

    def get(self, request, pk=None, **kwargs):
        self.__pk = pk
        if self.__pk is not None:
            obj = db_session.query(News).get(self.__pk)
            if obj is None:
                form.errors['pk'] = 'wrong_pk'
            setattr(self, '__obj', obj)
        return super(updateCRUDView, self).get(request, **kwargs)


    def post(self, request, pk=None, **kwargs):
        self.__pk = pk
        return super(updateCRUDView, self).post(request, **kwargs)


    def form_valid(self, form, *args, **kwargs):
        ##logging.error("DATA: %s" % form.cleaned_data)

        obj = News()
        if self.__pk is not None:
            obj = db_session.query(News).get(self.__pk)
            if obj is None:
                form.errors['pk'] = 'wrong_pk'
                return self.form_invalid(form)

        setattr(self, '__obj', obj)
        
        obj.disabled = False
        obj.owner_id = self.request.user.id

        obj.datebegin = form.cleaned_data['datebegin']
        obj.name = form.cleaned_data['name']
        obj.description = form.cleaned_data['description']
        obj.body = form.cleaned_data['body']
        
        db_session.add(obj)
        db_session.commit()

        return ResponseRedirect(url_for('news:crud_update', pk=obj.id))



    def form_invalid(self, form, *args, **kwargs):
        kwargs['form'] = form
        data = self.render_template(*args, **kwargs)
        return Response(data)




class deleteCRUDView(AccessMixin, View):
    access_group = 'admin'

    def get(self, request, pk, **kwargs):
        obj = db_session.query(News).filter(News.id==pk)
        obj.delete()
        db_session.commit()
        return ResponseRedirect(url_for('news:crud_list'))

