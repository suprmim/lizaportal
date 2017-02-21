from sqlalchemy import Table, MetaData, Column, Integer, VARCHAR
from sqlalchemy import ForeignKey, TEXT
from sqlalchemy.orm import mapper,relationship
from utils.db import get_metadata

from models.articles_content_categories.sa_models import ArticleContentCategory


metadata = get_metadata()


## MODEL:
class ContentArticle(object):
    def __init__(self, url_ident, name, body, keywords, style_path):
        self.url_ident = url_ident
        self.name = name
        self.body = body
        self.style_path = style_path
        self.keywords = keywords


content_article = Table('content_article', metadata,
    Column('id', Integer, primary_key=True, nullable=False, unique=True),
    Column('url_ident', VARCHAR(255), nullable=False, server_default=''),
    Column('name', TEXT, nullable=False, server_default=''),
    Column('body', TEXT, nullable=True),
    Column('keywords', TEXT, nullable=True),
    Column('style_path', VARCHAR(255)),
    extend_existing=True,
)


mapper(ContentArticle, content_article, properties={
        'article_cat_articles': relationship(ArticleContentCategory, backref='content_article',
            order_by=ArticleContentCategory.id, cascade='all,delete,delete-orphan'),
    },
    primary_key=[content_article.c.id],
)

