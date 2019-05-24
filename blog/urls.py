from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', view=views.index, name='index'),
    url(r'^article/(?P<article_id>[0-9]+)/$', view=views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)/$', view=views.article_edit, name='article_edit'),
    url(r'^edit/action/*', view=views.edit_action, name='edit_action'),
]
