from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.datas.views',
    url(r'^$', 'datas', name='datas'),
    url(r'^excel', 'export_excel', name='export_excel'),

)


