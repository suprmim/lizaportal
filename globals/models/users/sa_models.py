from sqlalchemy import Table, MetaData, Column, Integer, VARCHAR, ForeignKey, DateTime
from sqlalchemy.orm import mapper,relationship
from sqlalchemy.sql import func

from sqlalchemy import DECIMAL, Boolean,Float
from sqlalchemy.sql.expression import false as sa_false

from utils.db import get_metadata

from models.users_groups.sa_models import UsersGroups
from models.seminar_users.sa_models import SeminarUsers

metadata = get_metadata()


## MODEL:
class Users(object):
    def __init__(self, login, passwd=None, email=None, disabled=False, 
        fio='', phone='', validation_code=None, validated=False
    ):
        self.login = login
        self.passwd = passwd
        self.email = email
        self.fio = fio
        self.phone = phone
        self.crdate = func.now()
        self.validation_code = validation_code
        self.validated = validated
        self.disabled = disabled


users = Table('users', metadata,
    Column('id', Integer, primary_key=True, nullable=False, unique=True),
    Column('crdate', DateTime(timezone=True), nullable=False, server_default=func.now()),
    Column('login', VARCHAR(255), nullable=False),
    Column('passwd', VARCHAR(255), nullable=True),
    Column('email', VARCHAR(255), nullable=True),
    Column('fio', VARCHAR(255), nullable=False, server_default=''),
    Column('phone', VARCHAR(32), nullable=False, server_default=''),
    Column('validation_code', VARCHAR(255), nullable=True),
    Column('validated', Boolean(), nullable=False, server_default=sa_false()),
    Column('disabled', Boolean(), nullable=False, server_default=sa_false()),
    extend_existing=True,
)


mapper(Users, users, properties={         
        'users_ugrp': relationship(UsersGroups, backref='user',
            order_by=UsersGroups.id, cascade='all,delete,delete-orphan'),
        'users_seminars': relationship(SeminarUsers, backref='user',
            order_by=SeminarUsers.id, cascade='all,delete,delete-orphan'),
    },  
    primary_key=[users.c.id],
)


