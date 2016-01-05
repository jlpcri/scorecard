from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.personals.views',
    url(r'^$', 'personals', name='personals'),
    url(r'^weekly_personal_new_manually', 'weekly_personal_stats_new_manually', name='weekly_personal_stats_new_manually'),
)


