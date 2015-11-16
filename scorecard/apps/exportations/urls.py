from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.exportations.views',
    url(r'^$', 'exportations', name='exportations'),

)


