import datetime, pytz
from sqlalchemy import Table, MetaData, Column, Integer, VARCHAR, ForeignKey, DateTime, TEXT
from sqlalchemy.orm import mapper,relationship
from sqlalchemy.sql import func

from sqlalchemy import DECIMAL, Boolean,Float
from sqlalchemy.sql.expression import false as sa_false

from utils.db import get_metadata

from models.seminar_users.sa_models import SeminarUsers

metadata = get_metadata()


## MODEL:
class Seminars(object):
    def __init__(self, datebegin=func.now(), name=None, description='', capacity=0, 
        price=0, owner_id=None, disabled=False, body='',
    ):
        self.datebegin = datebegin
        self.name = name
        self.description = description
        self.body = body
        self.crdate = func.now()
        self.disabled = disabled
        self.capacity = capacity
        self.owner_id = owner_id
        self.price = price

    @prototype
    def is_expired(self):
        ## Get current datetime in UTC:
        dt = datetime.datetime.now().replace(tzinfo=pytz.utc)
        if (self.datebegin - dt).days < 0:
            return True
        return False


seminars = Table('seminars', metadata,
    Column('id', Integer, primary_key=True, nullable=False, unique=True),
    Column('crdate', DateTime(timezone=True), nullable=False, server_default=func.now()),
    Column('datebegin', DateTime(timezone=True), nullable=False),
    Column('name', VARCHAR(255), nullable=False),
    Column('price', Integer, nullable=False, server_default='0'),
    Column('capacity', Integer, nullable=False, server_default='0'),
    Column('disabled', Boolean(), nullable=False, server_default=sa_false()),
    Column('owner_id', Integer, ForeignKey('users.id'), nullable=False),
    Column('description', TEXT, nullable=False, server_default=''),
    Column('body', TEXT, nullable=False, server_default=''),
    extend_existing=True,
)


mapper(Seminars, seminars, properties={         
        'visitors': relationship(SeminarUsers, backref='seminar',
            order_by=SeminarUsers.id, cascade='all,delete,delete-orphan'),
    },  
    primary_key=[seminars.c.id],
)


