from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url('new', views.article_list, name='new'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='detail'),
  ]

