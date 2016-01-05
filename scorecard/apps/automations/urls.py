from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.automations.views',
    url(r'^$', 'automations', name='automations'),

)


