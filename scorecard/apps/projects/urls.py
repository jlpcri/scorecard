from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.projects.views',
    url(r'^$', 'projects', name='projects'),

)
