from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('', 
	#index
	url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^(?P<slug>[\w\-]+)/$', views.PostView.as_view(), name='posts'),               
	)
