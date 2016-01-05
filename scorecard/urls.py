"""scorecard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = [
    url(r'^scorecard/$', 'scorecard.apps.core.views.landing', name='landing'),
    url(r'^scorecard/automations/', include('scorecard.apps.automations.urls', namespace='automations')),
    url(r'^scorecard/datas/', include('scorecard.apps.datas.urls', namespace='datas')),
    url(r'^scorecard/help/', include('scorecard.apps.help.urls', namespace='help')),
    url(r'^scorecard/personals/', include('scorecard.apps.personals.urls', namespace='personals')),
    url(r'^scorecard/projects/', include('scorecard.apps.projects.urls', namespace='projects')),
    url(r'^scorecard/teams/', include('scorecard.apps.teams.urls', namespace='teams')),
    url(r'^scorecard/', include('scorecard.apps.users.urls', namespace='users')),

    url(r'^scorecard/admin/', include(admin.site.urls)),
]
