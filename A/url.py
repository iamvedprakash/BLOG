from django.conf.urls import url
from . import views

app_name = 'article'
urlpatterns = [

    url(r'^app$', views.list, name="list"),
    url(r'^create/$', views.create_article, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_details, name="detail"), #http://127.0.0.1:8000/A/django-rules/
]
