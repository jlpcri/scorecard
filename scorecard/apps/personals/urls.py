from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.personals.views',
    url(r'^$', 'personals', name='personals'),
    url(r'^weekly_personal_new_manually/$', 'weekly_personal_stats_new_manually', name='weekly_personal_stats_new_manually'),
    url(r'^personal_stats/(?P<stats_id>\d+)/$', 'personal_stats', name='personal_stats'),
    url(r'^personal_stats_edit/(?P<stats_id>\d+)/$', 'personal_stats_edit', name='personal_stats_edit'),
)


