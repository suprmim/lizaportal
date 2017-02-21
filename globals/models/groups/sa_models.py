from sqlalchemy import Table, MetaData, Column, Integer, VARCHAR, ForeignKey
from sqlalchemy import DECIMAL, Boolean,Float
from sqlalchemy.orm import mapper,relationship
from sqlalchemy.sql.expression import false as sa_false

from utils.db import get_metadata

from models.users_groups.sa_models import UsersGroups


metadata = get_metadata()


## MODEL:
class Groups(object):
    def __init__(self, name, disabled=False):
        self.name = name
        self.disabled = disabled


groups = Table('groups', metadata,
    Column('id', Integer, primary_key=True, nullable=False, unique=True),
    Column('name', VARCHAR(100), nullable=False),
    Column('disabled', Boolean(), nullable=False, server_default=sa_false()),
    extend_existing=True,
)


mapper(Groups, groups, properties={
        'groups_ugrp': relationship(UsersGroups, backref='groups',
            order_by=UsersGroups.id, cascade='all,delete,delete-orphan'),
    },
    primary_key=[groups.c.id],
)



