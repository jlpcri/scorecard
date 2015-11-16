from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.teams.views',
    url(r'^$', 'teams', name='teams'),

)


