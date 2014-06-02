from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('', 
	#index
	url(r'^$', views.IndexView.as_view(), name='index'),
	)
