import sha
from flaskcbv.forms import Form

from utils.db import get_db_session
from models.users.sa_models import Users as UsersModel
from models.groups.sa_models import Groups as GroupsModel
from models.users_groups.sa_models import UsersGroups as UsersGroupsModel


## Init session
#session = get_db_session(echo=True)
session = get_db_session(echo=False)




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
        super(LoginForm, self).clean()
        if not self.is_clean:
            return None

        ## Check username and password:
        user = session.query(UsersModel).filter(UsersModel.login==self.cleaned_data['username']).first()
        if user is None:
            self.errors['username'] = 'wrong_user_or_passwd'
            return None

        if not self.cleaned_data['passwd'] == user.passwd:
            self.errors['username'] = 'wrong_user_or_passwd'
            return None


