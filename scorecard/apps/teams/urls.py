from django.conf.urls import url

from scorecard.apps.teams import views

urlpatterns = [
    url(r'^$', views.teams, name='teams'),
    url(r'^metric_detail/(?P<metric_id>\d+)/$', views.metric_detail, name='metric_detail'),
    url(r'^metric_edit/(?P<metric_id>\d+)/$', views.metric_edit, name='metric_edit'),

    url(r'^weekly_metric_new_manually/$', views.weekly_metric_new_manually, name='weekly_metric_new_manually'),
    url(r'^send_email/$', views.send_email, name='send_email'),

    url(r'^fetch_team_members_by_date/$', views.fetch_team_members_by_date, name='fetch_team_members_by_date'),
    url(r'^collect_data', views.collect_data, name='collect_data'),

    url(r'^add_product_quality_chart?$', views.add_product_quality_chart, name='add_product_quality_chart'),
    url(r'^delete_product_quality_chart?$', views.delete_product_quality_chart, name='delete_product_quality_chart'),

    url(r'^add_quality_assurance_chart?$', views.add_quality_assurance_chart, name='add_quality_assurance_chart'),
    url(r'^delete_quality_assurance_chart?$', views.delete_quality_assurance_chart, name='delete_quality_assurance_chart'),

    url(r'^add_quality_innovation_chart?$', views.add_quality_innovation_chart, name='add_quality_innovation_chart'),
    url(r'^delete_quality_innovation_chart?$', views.delete_quality_innovation_chart, name='delete_quality_innovation_chart'),

    url(r'^add_requirements_engineering_chart?$', views.add_requirements_engineering_chart, name='add_requirements_engineering_chart'),
    url(r'^delete_requirements_engineering_chart?$', views.delete_requirements_engineering_chart, name='delete_requirements_engineering_chart'),

    url(r'^add_test_engineering_chart?$', views.add_test_engineering_chart, name='add_test_engineering_chart'),
    url(r'^delete_test_engineering_chart?$', views.delete_test_engineering_chart, name='delete_test_engineering_chart'),

    url(r'^add_test_lab_chart?$', views.add_test_lab_chart, name='add_test_lab_chart'),
    url(r'^delete_test_lab_chart?$', views.delete_test_lab_chart, name='delete_test_lab_chart'),
]


