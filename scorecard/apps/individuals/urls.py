from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.individuals.views',
    url(r'^$', 'individuals', name='individuals'),

)


