from django.conf.urls import url

from scorecard.apps.datas import views

urlpatterns = [
    url(r'^$', views.datas, name='datas'),
    url(r'^excel', views.export_excel, name='export_excel'),

]
