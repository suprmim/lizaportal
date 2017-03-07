from sqlalchemy import Table, MetaData, Column, Integer, VARCHAR
from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import mapper

from utils.db import get_metadata

metadata = get_metadata()


## MODEL:
class SeminarUsers(object):
    def __init__(self, user_id, group_id):
        self.user_id = user_id
        self.group_id = group_id

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

