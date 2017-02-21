from sqlalchemy import Table, MetaData, Column, Integer, VARCHAR
from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import mapper

from utils.db import get_metadata

metadata = get_metadata()


## MODEL:
class UsersGroups(object):
    def __init__(self, user_id, group_id):
        self.user_id = user_id
        self.group_id = group_id

users_groups = Table('users_groups', metadata,
    Column('id', Integer, primary_key=True, nullable=False, unique=True),
    Column('user_id', Integer, ForeignKey('users.id'), 
                          nullable=False),
    Column('group_id', Integer, ForeignKey('groups.id'), 
                          nullable=False), 
    extend_existing=True,
)


mapper(UsersGroups, users_groups, 
        primary_key=[users_groups.c.id],
)

