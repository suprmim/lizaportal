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
from models.seminars.sa_models import Seminars
from models.seminar_users.sa_models import SeminarUsers


from misc.tzinfo import myTimeZone


db_session = get_db_session(echo=False)

from .forms import updateCRUDForm

class listViewMixin(object):

    def get_query(self):
        stmt = db_session.query(SeminarUsers.seminar_id, sa_func.count('id').label('assigned')).group_by(SeminarUsers.seminar_id).subquery()
	main_query = db_session.query(Seminars, stmt.c.assigned).outerjoin(stmt, Seminars.id==stmt.c.seminar_id)
        main_query = main_query.order_by(desc(Seminars.datebegin))
        return main_query


class listView(listViewMixin, AuthedMixin, TemplateView):
    template='seminars/list.tpl'

    def get_context_data(self, **kwargs):
        context = super(listView, self).get_context_data(**kwargs)
        context['seminars'] = self.get_query()
        context['is_mylist'] = False
        return context



class myListView(listViewMixin, AuthedMixin, TemplateView):
    template='seminars/list.tpl'

    def get_context_data(self, **kwargs):
        context = super(myListView, self).get_context_data(**kwargs)
        su = aliased(SeminarUsers)
        qs = self.get_query()
        qs = qs.join(su, su.seminar_id==Seminars.id)
        qs = qs.filter(su.user_id==self.request.user.id)
        context['seminars'] = qs
        context['is_mylist'] = True
        return context



class detailsView(AuthedMixin, TemplateView):
    template='seminars/details.tpl'

    def get_context_data(self, **kwargs):
        context = super(detailsView, self).get_context_data(**kwargs)
        context['seminar'] = db_session.query(Seminars).get(self.__pk)
        return context

    def get(self, request, pk, **kwargs):
        self.__pk  = pk
        return super(detailsView, self).get(request, **kwargs)



class assignView(LoginRequiredMixin, View):
    def __init__(self, *args, **kwargs):
        self.assign = kwargs.pop('assign')
        super(assignView, self).__init__(*args, **kwargs)

    def get(self, request, pk, **kwargs):
        seminar = db_session.query(Seminars).get(pk)

        ## No such seminar:
        if seminar is None:
            return ResponseRedirect(url_for('seminars:list', pk=pk))

        ## Get seminar->user relation:
        su = db_session.query(SeminarUsers).filter(SeminarUsers.seminar_id==seminar.id)
        su = su.filter(SeminarUsers.user_id==self.request.user.id)

        ## Allready assigned:
        if self.assign and su.first() is not None:
            return ResponseRedirect(url_for('seminars:details', pk=pk))

        ## Allready not assigned:
        elif not self.assign and su.first() is None:
            return ResponseRedirect(url_for('seminars:details', pk=pk))

        ## Assign user to seminar:
        if self.assign:
            ## Too many listners:
            if not seminar.user_assigne_avalible:
                return ResponseRedirect(url_for('seminars:details', pk=pk))

            su = SeminarUsers()
            su.user_id = self.request.user.id
            su.seminar_id = seminar.id
            db_session.add(su)

        ## UnAssign user:
        else:
            su.delete()

        db_session.commit()
        
        return ResponseRedirect(url_for('seminars:details', pk=pk))



class listCRUDView(AccessMixin, TemplateView):
    template='seminars/crud_list.tpl'
    access_group = 'admin'

    def get_context_data(self, **kwargs):
        context = super(listCRUDView, self).get_context_data(**kwargs)
        context['seminars'] = db_session.query(Seminars).order_by(desc(Seminars.datebegin)).all()
        return context


class updateCRUDView(AccessMixin, FormViewMixin, TemplateView):
    template='seminars/crud_update.tpl'
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
            obj = db_session.query(Seminars).get(self.__pk)
            if obj is None:
                form.errors['pk'] = 'wrong_pk'
            setattr(self, '__obj', obj)
        return super(updateCRUDView, self).get(request, **kwargs)


    def post(self, request, pk=None, **kwargs):
        self.__pk = pk
        return super(updateCRUDView, self).post(request, **kwargs)


    def form_valid(self, form, *args, **kwargs):
        ##logging.error("DATA: %s" % form.cleaned_data)

        obj = Seminars()
        if self.__pk is not None:
            obj = db_session.query(Seminars).get(self.__pk)
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
        obj.capacity = form.cleaned_data['capacity']
        obj.price = form.cleaned_data['price']
        
        db_session.add(obj)
        db_session.commit()

        return ResponseRedirect(url_for('seminars:crud_update', pk=obj.id))



    def form_invalid(self, form, *args, **kwargs):
        kwargs['form'] = form
        data = self.render_template(*args, **kwargs)
        return Response(data)




class deleteCRUDView(AccessMixin, View):
    access_group = 'admin'

    def get(self, request, pk, **kwargs):
        obj = db_session.query(Seminars).filter(Seminars.id==pk)
        obj.delete()
        db_session.commit()
        return ResponseRedirect(url_for('seminars:crud_list'))

