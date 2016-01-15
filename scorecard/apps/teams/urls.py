from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('scorecard.apps.teams.views',
    url(r'^$', 'teams', name='teams'),
    url(r'^metric_detail/(?P<metric_id>\d+)/$', 'metric_detail', name='metric_detail'),
    url(r'^metric_edit/(?P<metric_id>\d+)/$', 'metric_edit', name='metric_edit'),

    url(r'^weekly_metric_new_manually/$', 'weekly_metric_new_manually', name='weekly_metric_new_manually'),

    url(r'^add_product_quality_chart?$', 'add_product_quality_chart', name='add_product_quality_chart'),
    url(r'^delete_product_quality_chart?$', 'delete_product_quality_chart', name='delete_product_quality_chart'),

    url(r'^add_quality_assurance_chart?$', 'add_quality_assurance_chart', name='add_quality_assurance_chart'),
    url(r'^delete_quality_assurance_chart?$', 'delete_quality_assurance_chart', name='delete_quality_assurance_chart'),

    url(r'^add_quality_innovation_chart?$', 'add_quality_innovation_chart', name='add_quality_innovation_chart'),
    url(r'^delete_quality_innovation_chart?$', 'delete_quality_innovation_chart', name='delete_quality_innovation_chart'),

    url(r'^add_requirements_engineering_chart?$', 'add_requirements_engineering_chart', name='add_requirements_engineering_chart'),
    url(r'^delete_requirements_engineering_chart?$', 'delete_requirements_engineering_chart', name='delete_requirements_engineering_chart'),

    url(r'^add_test_engineering_chart?$', 'add_test_engineering_chart', name='add_test_engineering_chart'),
    url(r'^delete_test_engineering_chart?$', 'delete_test_engineering_chart', name='delete_test_engineering_chart'),

    url(r'^add_test_lab_chart?$', 'add_test_lab_chart', name='add_test_lab_chart'),
    url(r'^delete_test_lab_chart?$', 'delete_test_lab_chart', name='delete_test_lab_chart'),

)


