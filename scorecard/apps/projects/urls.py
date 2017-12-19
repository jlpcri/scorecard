from django.conf.urls import url

from scorecard.apps.projects import views

urlpatterns = [
       url(r'^$', views.projects, name='projects'),
       url(r'^new/$', views.project_new, name='project_new'),
       url(r'^edit/$', views.project_edit, name='project_edit'),

       url(r'^project_phase/new/$', views.project_phase_new, name='project_phase_new'),
       url(r'^project_phase/edit/$', views.project_phase_edit, name='project_phase_edit'),

       url(r'^ticket/new/$', views.ticket_new, name='ticket_new'),
       url(r'^ticket/edit/$', views.ticket_edit, name='ticket_edit'),

       url(r'^fetch_workers/$', views.fetch_workers, name='fetch_workers'),

]
