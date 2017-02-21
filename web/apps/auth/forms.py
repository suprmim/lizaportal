import sha
import logging
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

        ## Creating new session in redis:
        session_ = Sessions().create(user.id)
        flask_session['session'] = session_
        self.view.request.user = user
        self.view.request.session = session_

