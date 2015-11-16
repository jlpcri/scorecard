from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.congregations.views',
    url(r'^$', 'congregations', name='congregations'),

)


