import json
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.template import RequestContext

from models import HumanResource, FunctionalGroup

from scorecard.apps.users.models import FunctionalGroup

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@login_required
def home(request):

    functional_groups = FunctionalGroup.objects.all()

    for functional_group in functional_groups:
        if functional_group.key == 'PQ':
            product_quality = functional_group.testmetrics_set.all()
        elif functional_group.key == 'QA':
            quality_assurance = functional_group.testmetrics_set.all()
        elif functional_group.key == 'QI':
            quality_innovation = functional_group.innovationmetrics_set.all()
        elif functional_group.key == 'RE':
            requirements_engineering = functional_group.requirementmetrics_set.all()
        elif functional_group.key == 'TE':
            test_engineering = functional_group.testmetrics_set.all()
        elif functional_group.key == 'TL':
            test_lab = functional_group.labmetrics_set.all()

    # return render(request, 'users/home.html')
    return render(request, 'users/home.html',
                  { 'product_quality': product_quality,
                    'quality_assurance': quality_assurance,
                    'quality_innovation': quality_innovation,
                    'requirements_engineering': requirements_engineering,
                    'test_engineering': test_engineering,
                    'test_lab': test_lab } )

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
                    HumanResource.objects.get(user=user)
                except HumanResource.DoesNotExist:
                    HumanResource.objects.create(user=user)
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
            '-last_login'
        ]
        users = ''
        sort = request.GET.get('sort', '')
        sort = sort if sort else 'username'

        if sort in sort_types:
            users = User.objects.all().order_by(sort)

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

@user_passes_test(user_is_manager)
def user_manager_assign(request):
    user = request.user
    key = request.user.humanresource.functional_group.key

    if request.method == 'GET':
        users = User.objects.all().order_by('username')
        if user.is_superuser:
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
