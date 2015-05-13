from django.conf.urls import patterns, url
from manual import views

urlpatterns = patterns('',
                       # index
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^list/$', views.List.as_view(), name='list'),
                       url(r'^(?P<slug>[\w\-]+)/$',
                           views.PostView.as_view(), name='posts'),
                       )
