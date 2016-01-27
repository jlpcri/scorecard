from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.users.views',
    url(r'^home/$', 'home', name='home'),
    url(r'^signin/$', 'sign_in', name='sign_in'),
    url(r'^signout/$', 'sign_out', name='sign_out'),
    url(r'^user_management/$', 'user_management', name='management'),
    url(r'^user_manager_assign/$', 'user_manager_assign', name='manager_assign'),
    url(r'^user_manager_check/$', 'user_manager_check', name='user_manager_check'),

    url(r'^user_team_assign/$', 'user_team_assign', name='team_assign'),

    url(r'^add_home_chart?$', 'add_home_chart', name='add_home_chart'),
    url(r'^delete_home_chart?$', 'delete_home_chart', name='delete_home_chart'),
    url(r'^update_user_chart_preferences?$', 'update_user_chart_preferences', name='update_user_chart_preferences'),
)

