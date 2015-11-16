from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.help.views',
    url(r'^$', 'guide', name='guide'),

)


