from django.conf.urls import url

from scorecard.apps.help import views

urlpatterns = [
    url(r'^$', views.guide, name='guide'),

]


