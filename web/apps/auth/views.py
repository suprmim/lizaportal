import logging
import datetime

from flaskcbv.view import TemplateView
from flaskcbv.view.crud import FormViewMixin

from .forms import LoginForm

class authView(FormViewMixin, TemplateView):
    template='auth/auth.tpl'
    form_class=LoginForm


    """
    ## Let's Redefine POST processing:
    def post(self, *args, **kwargs):

        ## Create our form object:
        form = self.get_form()

        ## Check form, this will run form.clean that will start 'clean_ATTR' methods, like in django
        if form.validate():
            ## By default it's a redirect to self.form_success_url or self.get_from_success_url():
            return self.form_valid(form)

        else:
            ## By default returns template with 'form' context variable:
            return self.form_invalid(form)
    """



