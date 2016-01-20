import json
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.template import RequestContext

from models import HumanResource, FunctionalGroup


@login_required
def home(request):
    return render(request, 'users/home.html')


def user_is_superuser(user):
    return user.is_superuser


def user_is_manager(user):
    return user.is_superuser or user.humanresource.manager


def user_manager_check(request):
    data = {}
    user_id = request.GET.get('user_id', '')
    user = User.objects.get(pk=user_id)
    data['group'] = user.humanresource.functional_group.id

    if user.humanresource.manager:
        data['manager'] = True
    else:
        data['manager'] = False

    return HttpResponse(json.dumps(data), content_type='application/json')


def sign_in(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            if user.is_active:
                login(request, user)
                try:
                    hr = HumanResource.objects.get(user=user)
                    if not hr.functional_group:
                        if user.is_superuser:
                            pass
                        elif hr.manager:
                            messages.error(request, 'Please <a href=\'{0}user_manager_assign\'>assign yourself </a> to your team.'.format(settings.LOGIN_URL))
                        else:
                            messages.error(request, 'Please ask your Supervisor to assign yourself to your team.')
                except HumanResource.DoesNotExist:
                    HumanResource.objects.create(user=user)
                    messages.error(request, 'Please ask your Supervisor to assign you to your team.')
                if request.GET.get('next'):
                    return redirect(request.GET['next'])
                else:
                    return redirect('users:home')
            else:
                messages.error(request, 'This account is inactive.')
                return redirect('landing')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('landing')
    else:
        return redirect('landing')


@login_required
def sign_out(request):
    logout(request)
    return redirect('landing')


@user_passes_test(user_is_superuser)
def user_management(request):
    if request.method == 'GET':
        sort_types = [
            'username',
            '-username',
            'last_login',
            '-last_login',
            'humanresource__functional_group__key',
            '-humanresource__functional_group__key'
        ]
        users = ''
        sort = request.GET.get('sort', '')
        sort = sort if sort else 'username'

        if sort in sort_types:
            if sort in ['humanresource__functional_group__key', '-humanresource__functional_group__key']:
                users = User.objects.order_by(sort, 'username')
            else:
                users = User.objects.order_by(sort)

        context = RequestContext(request, {
            'users': users,
            'sort': sort,
        })

        return render(request, 'users/user_management.html', context)


@user_passes_test(user_is_manager)
def user_manager_assign(request):
    user = request.user
    try:
        key = request.user.humanresource.functional_group.key
    except AttributeError:
        key = ''

    if request.method == 'GET':
        users = User.objects.all().order_by('username')
        if user.is_superuser or not key:
            groups = FunctionalGroup.objects.all().order_by('name')
        else:
            groups = FunctionalGroup.objects.filter(key=key)

        context = RequestContext(request, {
            'users': users,
            'groups': groups,
            'first_check': users[0].humanresource.manager
        })

        return render(request, 'users/user_manager_assign.html', context)

    elif request.method == 'POST':
        user_id = request.POST.get('user_select', '')
        group_id = request.POST.get('group_select', '')
        is_manager = request.POST.get('is_manager', '')

        user = User.objects.get(id=user_id)
        user.humanresource.functional_group = FunctionalGroup.objects.get(pk=group_id)
        if is_manager:
            user.humanresource.manager = True
        else:
            user.humanresource.manager = False

        user.humanresource.save()

        return redirect('users:home')
