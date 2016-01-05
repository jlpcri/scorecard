from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.personals.views',
    url(r'^$', 'individuals', name='personals'),

)


