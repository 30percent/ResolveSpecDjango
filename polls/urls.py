from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('', 
	#index
	url(r'^$', views.IndexView.as_view(), name='index'),
	#ex. /5/
	#(?P<poll_id>\d+): parens stores as param, ?P<poll_id> sets name \d+ is actual pattern
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	#ex. /5/results/
	url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	#ex. /5/vote
	url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
	)
