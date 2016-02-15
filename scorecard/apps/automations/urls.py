from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.automations.views',
    url(r'^$', 'automations', name='automations'),
    url(r'automation_detail/(?P<automation_id>\d+)/$', 'automation_detail', name='automation_detail'),
    url(r'automation_edit/(?P<automation_id>\d+)/$', 'automation_edit', name='automation_edit'),
    url(r'automation_new/$', 'automation_new', name='automation_new'),
    url(r'run_script/$', 'run_script', name='run_script'),
)


