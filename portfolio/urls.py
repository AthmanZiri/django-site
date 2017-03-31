from django.conf.urls import url
from .views import project_list, project_detail


urlpatterns = [

	url(r'^$', project_list, name='project_list'),

	url(r'^(?P<post_id>\d+)/$', project_detail, name='project_detail')
	
]