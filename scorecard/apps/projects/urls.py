from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.projects.views',
                       url(r'^$', 'projects', name='projects'),
                       url(r'^(?P<project_id>\d+)/$', 'project_detail', name='project_detail'),
                       url(r'^(?P<project_id>\d+)/edit/$', 'project_edit', name='project_edit'),
                       url(r'^new/$', 'project_new', name='project_new'),

                       url(r'ticket/(?P<ticket_id>\d+)/$', 'ticket_detail', name='ticket_detail'),
                       url(r'ticket/(?P<ticket_id>\d+)/edit/$', 'ticket_edit', name='ticket_edit'),
                       url(r'^ticket/new/$', 'ticket_new', name='ticket_new'),

)
