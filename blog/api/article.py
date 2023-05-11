from combojsonapi.event.resource import EventsResource
from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.extensions import db
from blog.models import Article
from blog.schemas import ArticleSchema


class ArticleEvent(EventsResource):
    def event_get_count(self):
        return {'count': Article.query.count()}


class ArticleDetailEvent(EventsResource):

    def event_get_count_by_author(self, author_id, *args, **kwargs):
        return {'count': Article.query.filter(Article.author_id == kwargs['id']).count()}


class ArticleList(ResourceList):
    events = ArticleEvent
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }


class ArticleDetail(ResourceDetail):
    events = ArticleDetailEvent
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }
