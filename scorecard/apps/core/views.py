from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect


def landing(request):
    if request.user.is_authenticated():
        return redirect('users:home')
    return render(request, 'core/landing.html')


def get_active_top_link(request):
    if request.path.startswith('/scorecard/projects'):
        active = 'projects'
    elif request.path.startswith('/scorecard/personal'):
        active = 'personal'
    elif request.path.startswith('/scorecard/team'):
        active = 'team'
    elif request.path.startswith('/scorecard/data'):
        active = 'data'
    elif request.path.startswith('/scorecard/automation'):
        active = 'automation'
    elif request.path.startswith('/scorecard/help'):
        active = 'help'
    else:
        active = 'home'

    return {'active': active}


def check_user_team(request):
    user = request.user
    if not user.humanresource.functional_group:
        if user.is_superuser:
            pass
        elif user.humanresource.manager:
            messages.error(request, 'Please <a href=\'{0}user_manager_assign\'>assign yourself </a> to a team.'.format(settings.LOGIN_URL))
        else:
            messages.error(request, 'Please ask your Supervisor to assign yourself to a team.')
