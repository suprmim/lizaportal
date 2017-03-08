from sqlalchemy import Table, MetaData, Column, Integer, VARCHAR
from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import mapper

from utils.db import get_metadata
from utils.db import get_db_session

metadata = get_metadata()


## MODEL:
class SeminarUsers(object):
    def __init__(self, user_id=None, seminar_id=None):
        self.user_id = user_id
        self.seminar_id = seminar_id

    @classmethod
    def get_user_seminars_query(cls, uid):
        db_session = get_db_session(echo=False)
        return db_session.query(cls).filter(cls.user_id==uid)

    @classmethod
    def get_user_seminars(cls, uid):
        for item in cls.get_user_seminars_query(uid):
            yield item.seminar


seminar_users = Table('seminar_users', metadata,
    Column('id', Integer, primary_key=True, nullable=False, unique=True),
    Column('seminar_id', Integer, ForeignKey('seminars.id'), 
                          nullable=False), 
    Column('user_id', Integer, ForeignKey('users.id'), 
                          nullable=False),
    extend_existing=True,
)


mapper(SeminarUsers, seminar_users, 
        primary_key=[seminar_users.c.id],
)

