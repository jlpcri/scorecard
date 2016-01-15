from django.conf.urls import patterns, url


urlpatterns = patterns('scorecard.apps.users.views',
    url(r'^home/$', 'home', name='home'),
    url(r'^signin/$', 'sign_in', name='sign_in'),
    url(r'^signout/$', 'sign_out', name='sign_out'),
    url(r'^user_management/$', 'user_management', name='management'),
    # url(r'^user_update/(?P<user_id>\d+)/$', 'user_update', name='user_update'),
    # url(r'^user_delete/(?P<user_id>\d+)/$', 'user_delete', name='user_delete'),
    #
    # url(r'^user_settings/$', 'user_settings', name='user_settings'),
    # url(r'^user_settings_update/$', 'user_settings_update', name='user_settings_update'),

    url(r'^add_home_chart?$', 'add_home_chart', name='add_home_chart'),
    url(r'^delete_home_chart?$', 'delete_home_chart', name='delete_home_chart'),
)

