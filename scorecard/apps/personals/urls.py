from django.conf.urls import url

from scorecard.apps.personals import views


urlpatterns = [
    url(r'^$', views.personals, name='personals'),
    url(r'^weekly_personal_new_manually/$', views.weekly_personal_stats_new_manually, name='weekly_personal_stats_new_manually'),
    url(r'^personal_stats/(?P<stats_id>\d+)/$', views.personal_stats, name='personal_stats'),
    url(r'^personal_stats_edit/(?P<stats_id>\d+)/$', views.personal_stats_edit, name='personal_stats_edit'),
    url(r'fetch_personals_by_date/$', views.fetch_personals_by_date, name='fetch_personals_by_date'),
    url(r'collect_data/$', views.collect_data, name='collect_data'),

]


