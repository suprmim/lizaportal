import sha
import re
import logging

from validate_email import validate_email

from flask import abort, url_for, session as flask_session

from flaskcbv.forms import Form
from utils.db import get_db_session
from models.users.sa_models import Users as UsersModel
from models.groups.sa_models import Groups as GroupsModel
from models.users_groups.sa_models import UsersGroups as UsersGroupsModel

from sessions import Sessions


## Init session
#db_session = get_db_session(echo=True)
db_session = get_db_session(echo=False)



class LoginForm(Form):


    def clean_username(self, value):
        if value is None:
            raise Exception("empty")
        value = u"%s" % value
        return value[0:250]

    def clean_passwd(self, value):
        if value is None:
            raise Exception("empty")
        value = u"%s" % value
        return sha.new(value[0:250]).hexdigest()




    def clean(self, *args, **kwargs):

        ## First of all, check user by session:
        if self.view.check_session():
            return None

        ## No session stored in cookies, check form data:
        super(LoginForm, self).clean()
        if not self.is_clean:
            return None

        ## Check username and password:
        user = db_session.query(UsersModel).filter(UsersModel.login==self.cleaned_data['username']).first()
        if user is None:
            self.errors['username'] = 'wrong_user_or_passwd'
            return None

        if not self.cleaned_data['passwd'] == user.passwd:
            self.errors['username'] = 'wrong_user_or_passwd'
            return None

        if user.disabled:
            self.errors['username'] = 'user_is_disabled'
            return None

        ## Save user into request:
        self.view.request.user = user



class RegisterForm(Form):

    re_valid_uname = re.compile('^[a-z0-9_.@-]+$')

    def clean_username(self, value):
        if value is None:
            raise Exception("empty")
        value = u"%s" % value.lower()
        if len(value) < 6 or len(value) > 32:
            raise Exception("length")

        if len(self.re_valid_uname.findall(value)) == 0:
            raise Exception("symbols")

        return value

    def clean_passwd(self, value):
        if value is None:
            raise Exception("empty")
        value = u"%s" % value
        if len(value) < 6 or len(value) > 32:
            raise Exception("length")
        return sha.new(value).hexdigest()

    def clean_passwd2(self, value):
        if value is None:
            raise Exception("empty")
        value = u"%s" % value
        return sha.new(value[0:250]).hexdigest()


    def clean_email(self, value):
        if value is None:
            raise Exception("empty")
        value = u"%s" % value[0:250]
        if not validate_email(value, check_mx=False, verify=False):
            raise Exception("symbols")

        return value

    def clean_fio(self, value):
        if value is None:
            raise Exception("empty")
        value = u"%s" % value
        return value[0:250]

    def clean_phone(self, value):
        if value is None:
            value = ''
        value = u"%s" % value
        return value[0:32]



    def clean(self, *args, **kwargs):

        ## First of all, check user by session:
        if self.view.check_session():
            self.errors['authed'] = 'All ready authed!'
            return None

        ## No session stored in cookies, check form data:
        super(RegisterForm, self).clean()
        if not self.is_clean:
            return None

        ## Check username and password:
        user = db_session.query(UsersModel).filter(UsersModel.login==self.cleaned_data['username']).first()
        if user is not None:
            self.errors['username'] = 'exist'

        if not self.cleaned_data['passwd'] == self.cleaned_data['passwd2']:
            self.errors['passwd'] = 'wrong'

        ## Check username and password:
        user = db_session.query(UsersModel).filter(UsersModel.email==self.cleaned_data['email']).first()
        if user is not None:
            self.errors['email'] = 'exist'

        ## Check username and password:
        if self.cleaned_data['phone'] != '':
            user = db_session.query(UsersModel).filter(UsersModel.phone==self.cleaned_data['phone']).first()
            if user is not None:
                self.errors['phone'] = 'exist'



