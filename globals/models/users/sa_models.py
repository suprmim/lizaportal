from sqlalchemy import Table, MetaData, Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import mapper,relationship

from sqlalchemy import DECIMAL, Boolean,Float
from sqlalchemy.sql.expression import false as sa_false

from utils.db import get_metadata

from models.users_groups.sa_models import UsersGroups

metadata = get_metadata()


## MODEL:
class Users(object):
    def __init__(self, login, passwd=None, email=None, disabled=False):
        self.login = login
        self.passwd = passwd
        self.email = email
        self.disabled = disabled


users = Table('users', metadata,
    Column('id', Integer, primary_key=True, nullable=False, unique=True),
    Column('login', VARCHAR(255), nullable=False),
    Column('passwd', VARCHAR(255), nullable=True),
    Column('email', VARCHAR(255), nullable=True),
    Column('disabled', Boolean(), nullable=False, server_default=sa_false()),
    extend_existing=True,
)


mapper(Users, users, properties={         
        'users_ugrp': relationship(UsersGroups, backref='users',
            order_by=UsersGroups.id, cascade='all,delete,delete-orphan'),
    },  
    primary_key=[users.c.id],
)


