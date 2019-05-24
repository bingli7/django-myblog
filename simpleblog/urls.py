from django.conf.urls import url
from . import views

urlpatterns = [
    # url(regex, view, name)
    url(r'^$', views.blog_index, name='blog_index'),
    # article/2
    url(r'^article/(?P<article_id>\d+)/$', views.article_page, name='article_page'),
    url(r'^article/(?P<article_id>\d+)/edit/$', views.edit_page, name='edit_page'),
    url(r'^article/edit_action/$', views.edit_action, name='edit_action'),
]

