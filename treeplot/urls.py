from django.conf.urls import patterns, include, url
from treeplot import views

urlpatterns = patterns('', 
	#index
	url(r'^$', views.treetest, name='index'),
        url(r'^getTree', views.treetest, name='getTree'),
	)
