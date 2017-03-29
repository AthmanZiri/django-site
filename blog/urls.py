from django.conf.urls import url
from . views import post_list, post_detail, portfolio, team
from main.views import index

urlpatterns = [ 

	url(r'^$', post_list, name='post_list'),
	url(r'^(?P<post_id>\d+)/$', post_detail, name='post_detail'),
	url(r'^portfolio/$', portfolio, name='portfolio'),
	url(r'^team/$', team, name='team'),
	url(r'^index/$', index, name='index'),
    
]