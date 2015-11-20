from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.teams.views',
    url(r'^$', 'teams', name='teams'),
    url(r'^metric_detail/(?P<metric_id>\d+)/$', 'metric_detail', name='metric_detail'),
    url(r'^metric_edit/(?P<metric_id>\d+)/$', 'metric_edit', name='metric_edit'),

    url(r'^weekly_metric_new_manually/$', 'weekly_metric_new_manually', name='weekly_metric_new_manually'),

)


