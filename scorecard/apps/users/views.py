import json
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import RequestContext

from models import HumanResource, FunctionalGroup, ColumnPreference

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import simplejson
from scorecard.apps.core.views import check_user_team


@login_required
def home(request):
    check_user_team(request)

    functional_groups = FunctionalGroup.objects.all()

    for functional_group in functional_groups:
        if functional_group.key == 'QA':
            qa_metrics = functional_group.testmetrics_set.order_by('-created')
        elif functional_group.key == 'QI':
            qi_metrics = functional_group.innovationmetrics_set.order_by('-created')
        elif functional_group.key == 'RE':
            re_metrics = functional_group.requirementmetrics_set.order_by('-created')
        elif functional_group.key == 'TE':
            te_metrics = functional_group.testmetrics_set.order_by('-created')
        elif functional_group.key == 'TL':
            tl_metrics = functional_group.labmetrics_set.order_by('-created')

    # build a list of the user column preferences on a per table basis
    qa_column_preferences = list(ColumnPreference.objects.all().filter(user=request.user, table_name='Quality Assurance'))
    qi_column_preferences = list(ColumnPreference.objects.all().filter(user=request.user, table_name='Quality Innovation'))
    re_column_preferences = list(ColumnPreference.objects.all().filter(user=request.user, table_name='Requirements Engineering'))
    te_column_preferences = list(ColumnPreference.objects.all().filter(user=request.user, table_name='Test Engineering'))
    tl_column_preferences = list(ColumnPreference.objects.all().filter(user=request.user, table_name='Test Lab'))

    qa_hide_list = []
    qi_hide_list = []
    re_hide_list = []
    te_hide_list = []
    tl_hide_list = []

    # the user might have created a ColumnPreferences but the hide list might be empty
    # this also covers the case where a ColumnPreferences has not been created
    for e in qa_column_preferences:
        qa_hide_list = e.hide_list

    for e in qi_column_preferences:
        qi_hide_list = e.hide_list

    for e in re_column_preferences:
        re_hide_list = e.hide_list

    for e in te_column_preferences:
        te_hide_list = e.hide_list

    for e in tl_column_preferences:
        tl_hide_list = e.hide_list

    qa_user_hide_list = simplejson.dumps(qa_hide_list)
    qi_user_hide_list = simplejson.dumps(qi_hide_list)
    re_user_hide_list = simplejson.dumps(re_hide_list)
    tl_user_hide_list = simplejson.dumps(te_hide_list)
    te_user_hide_list = simplejson.dumps(tl_hide_list)

    return render(request, 'users/home.html',
                  {
                      'qa_data': qa_metrics,
                      'qi_data': qi_metrics,
                      're_data': re_metrics,
                      'te_data': te_metrics,
                      'tl_data': tl_metrics,
                      'qa_user_hide_list': qa_user_hide_list,
                      'qi_user_hide_list': qi_user_hide_list,
                      're_user_hide_list': re_user_hide_list,
                      'te_user_hide_list': te_user_hide_list,
                      'tl_user_hide_list': tl_user_hide_list,
                  })


def user_is_superuser(user):
    return user.is_superuser


def user_is_manager(user):
    return user.is_superuser or user.humanresource.manager


def user_manager_check(request):
    data = {}
    user_id = request.GET.get('user_id', '')
    user = User.objects.get(pk=user_id)
    try:
        data['group'] = user.humanresource.functional_group.id
    except AttributeError:
        data['group'] = None

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
                except HumanResource.DoesNotExist:
                    HumanResource.objects.create(user=user)
                    request.session['first_log'] = True
                    return redirect('users:team_assign')

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


@csrf_exempt
def add_home_chart(request):
    return HttpResponse('')


@csrf_exempt
def delete_home_chart(request):
    return HttpResponse('')


@csrf_exempt
def update_user_chart_preferences(request):

    if request.method == 'POST':
        if request.is_ajax():

            table_name = request.POST.get('table_name')
            column_list_str = request.POST.get('column_list')

            db_table_name = ''

            if table_name == 'product_quality_table':
                db_table_name = 'Product Quality'
            elif table_name == 'quality_assurance_table':
                db_table_name = 'Quality Assurance'
            elif table_name == 'quality_innovation_table':
                db_table_name = 'Quality Innovation'
            elif table_name == 'requirements_engineering_table':
                db_table_name = 'Requirements Engineering'
            elif table_name == 'test_engineering_table':
                db_table_name = 'Test Engineering'
            elif table_name == 'test_lab_table':
                db_table_name = 'Test Lab'

            column_preferences = ColumnPreference.objects.all().filter(user=request.user, table_name=db_table_name)
            column_preferences.update(hide_list=column_list_str)



    return HttpResponse('')


            column_preferences = ColumnPreference.objects.all().filter(user=request.user, table_name=db_table_name)


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


@login_required
def user_team_assign(request):
    user = request.user
    first_log = request.session.pop('first_log', '')

    if request.method == 'GET':
        if first_log:
            groups = FunctionalGroup.objects.all().order_by('name')

            context = RequestContext(request, {
                'users': [user],
                'groups': groups
            })

            return render(request, 'users/user_team_assign.html', context)
        else:
            return redirect('users:home')
    elif request.method == 'POST':
        group_id = request.POST.get('group_select', '')

        hr = HumanResource.objects.get(user=user)
        hr.functional_group = FunctionalGroup.objects.get(pk=group_id)
        hr.save()

        return redirect('users:home')

