from sqlalchemy import Table, MetaData, Column, Integer, VARCHAR
from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import mapper

from utils.db import get_metadata

metadata = get_metadata()


## MODEL:
class ArticleContentCategory(object):
    def __init__(self, category_id, article_id):
        self.category_id = category_id
        self.article_id = article_id

article_content_category = Table('article_content_category', metadata,
    Column('id', Integer, primary_key=True, nullable=False, unique=True),
    Column('category_id', Integer, ForeignKey('content_category.id'), 
                          nullable=False),
    Column('article_id', Integer, ForeignKey('content_article.id'), 
                          nullable=False), 
    extend_existing=True,
)


mapper(ArticleContentCategory, article_content_category, 
        primary_key=[article_content_category.c.id],
)

