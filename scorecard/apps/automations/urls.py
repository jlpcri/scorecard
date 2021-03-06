from django.conf.urls import url

from scorecard.apps.automations import views


urlpatterns = [
    url(r'^$', views.automations, name='automations'),
    url(r'automation_detail/(?P<automation_id>\d+)/$', views.automation_detail, name='automation_detail'),
    url(r'automation_edit/(?P<automation_id>\d+)/$', views.automation_edit, name='automation_edit'),
    url(r'automation_new/$', views.automation_new, name='automation_new'),
    url(r'automation_push_personal_batch/$', views.automation_push_personal_batch, name='automation_push_personal_batch'),

    url(r'script_test/$', views.script_test, name='script_test'),
]


