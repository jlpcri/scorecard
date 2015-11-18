from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.teams.views',
    url(r'^$', 'teams', name='teams'),
    url(r'^qi_new/$', 'qi_new', name='qi_new'),
    url(r'^qi_detail/(?P<qi_id>\d+)/$', 'qi_detail', name='qi_detail'),
    url(r'^qi_edit/(?P<qi_id>\d+)/$', 'qi_edit', name='qi_edit'),

)


