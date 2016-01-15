from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.projects.views',
                       url(r'^$', 'projects', name='projects'),
                       url(r'^new/$', 'project_new', name='project_new'),
                       url(r'^edit/$', 'project_edit', name='project_edit'),

                       url(r'^project_phase/new/$', 'project_phase_new', name='project_phase_new'),
                       url(r'^project_phase/edit/$', 'project_phase_edit', name='project_phase_edit'),

                       url(r'^ticket/new/$', 'ticket_new', name='ticket_new'),
                       url(r'^ticket/edit/$', 'ticket_edit', name='ticket_edit'),

)
