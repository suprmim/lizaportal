import logging
import time, datetime

from flask import abort, url_for, session as session

from flaskcbv.response import Response, ResponseRedirect

from gsettings import settings as global_settings

from utils.db import get_db_session
from models.users.sa_models import Users as UsersModel

db_session = get_db_session(echo=False)


from .sessions import Sessions

class authMixin(object):
    def check_session(self):
        ## Allready checked:
        if hasattr(self.request, 'user') and self.request.user is not None:
            return True

        ## First of all, check user by session:
        session_ = 'session' in session.keys() and session['session'] or None
        uid = Sessions.check(session_)
        if uid is not None:
            user = db_session.query(UsersModel).filter(UsersModel.id==uid).first()
            if user is not None:
                self.request.user = user
                self.request.session = session_
                return True
        return False

    def authenticate(self):
        if not hasattr(self.request, 'user') or self.request.user is None:
            return False

        ## Creating new session in redis:
        session_ = Sessions().create(self.request.user.id)
        session['session'] = session_
        self.request.session = session_
        return True






