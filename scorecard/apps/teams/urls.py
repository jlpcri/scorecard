from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.teams.views',
    url(r'^$', 'teams', name='teams'),
    url(r'^qi_detail/(?P<qi_id>\d+)/$', 'qi_detail', name='qi_detail'),
    url(r'^qi_edit/(?P<qi_id>\d+)/$', 'qi_edit', name='qi_edit'),

    url(r'^weekly_metric_new_manually/$', 'weekly_metric_new_manually', name='weekly_metric_new_manually'),

)


