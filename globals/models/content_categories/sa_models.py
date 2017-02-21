from sqlalchemy import Table, MetaData, Column, Integer, Float, String 
from sqlalchemy import VARCHAR,ForeignKey, TEXT
from sqlalchemy.orm import mapper,relationship
from utils.db import get_metadata

from sqlalchemy.ext.declarative import declarative_base
from asa_mptt import DjangoSAMPTT

from models.articles_content_categories.sa_models import ArticleContentCategory

metadata = get_metadata()
Base = declarative_base(metadata=metadata)


##MODEL
class ContentCategory(Base, DjangoSAMPTT):
    __tablename__ = 'content_category'
    id = Column(Integer, primary_key=True)
    name = Column( VARCHAR(255), nullable=False, server_default='')
    description = Column(TEXT, nullable=True)
    __table_args__ = {'extend_existing': True}

    def __repr__(self):
        return u"%s" % self.name

    category_cat_articles = relationship(
        ArticleContentCategory, backref = 'content_category'
    )

