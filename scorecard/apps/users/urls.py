from django.conf.urls import url

from scorecard.apps.users import views


urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^signin/$', views.sign_in, name='sign_in'),
    url(r'^signout/$', views.sign_out, name='sign_out'),
    url(r'^user_management/$', views.user_management, name='management'),
    url(r'^user_manager_assign/$', views.user_manager_assign, name='manager_assign'),
    url(r'^user_manager_check/$', views.user_manager_check, name='user_manager_check'),

    url(r'^user_team_assign/$', views.user_team_assign, name='team_assign'),

    url(r'^add_home_chart?$', views.add_home_chart, name='add_home_chart'),
    url(r'^delete_home_chart?$', views.delete_home_chart, name='delete_home_chart'),
    url(r'^update_user_chart_preferences?$', views.update_user_chart_preferences, name='update_user_chart_preferences'),
    url(r'^temp/$', views.temp, name='temp'),
]

