import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext

from models import TestMetrics, RequirementMetrics, InnovationMetrics, LabMetrics, TestMetricsConfiguration
from forms import InnovationForm, LabForm, RequirementForm, TestForm
from scorecard.apps.core.views import check_user_team
from scorecard.apps.personals.models import TestStats, InnovationStats, RequirementStats, LabStats
from scorecard.apps.users.views import user_is_superuser, user_is_manager
from tasks import weekly_metric_new, weekly_send_email
from utils import context_teams

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@login_required
def teams(request):
    check_user_team(request)

    context = RequestContext(request, context_teams(request))

    return render(request, 'teams/teams.html', context)


@login_required
@user_passes_test(user_is_superuser)
def weekly_metric_new_manually(request):
    """
    Manually add new metric
    :param request:
    :return:
    """

    result = weekly_metric_new()
    if not result['valid']:
        messages.error(request, result['message'])

    return HttpResponseRedirect(reverse('teams:teams'))


@login_required
@user_passes_test(user_is_superuser)
def send_email(request):
    weekly_send_email()

    return HttpResponseRedirect(reverse('teams:teams'))


@login_required
@user_passes_test(user_is_manager)
def metric_detail(request, metric_id):
    key = request.GET.get('key', '')
    try:
        test_metric_config = TestMetricsConfiguration.objects.get(functional_group__key=key)
    except TestMetricsConfiguration.DoesNotExist:
        test_metric_config = ''

    if key in ['QA', 'TE']:
        metric = get_object_or_404(TestMetrics, pk=metric_id)
        form = TestForm(instance=metric)
    elif key == 'QI':
        metric = get_object_or_404(InnovationMetrics, pk=metric_id)
        form = InnovationForm(instance=metric)
    elif key == 'RE':
        metric = get_object_or_404(RequirementMetrics, pk=metric_id)
        form = RequirementForm(instance=metric)
    elif key == 'TL':
        metric = get_object_or_404(LabMetrics, pk=metric_id)
        form = LabForm(instance=metric)
    else:
        messages.error(request, 'No key to Functional Group found')
        return redirect('teams:teams')

    # qi = get_object_or_404(InnovationMetrics, pk=qi_id)
    # form = InnovationForm(instance=qi)
    context = RequestContext(request, {
        'metric': metric,
        'form': form,
        'test_metric_config': test_metric_config
    })

    return render(request, 'teams/metric_detail.html', context)


@login_required
@user_passes_test(user_is_manager)
def metric_edit(request, metric_id):
    key = request.GET.get('key', '')

    if request.method == 'POST':
        if key in ['QA', 'TE']:
            metric = get_object_or_404(TestMetrics, pk=metric_id)
            form = TestForm(request.POST, instance=metric)
        elif key == 'QI':
            metric = get_object_or_404(InnovationMetrics, pk=metric_id)
            form = InnovationForm(request.POST, instance=metric)
        elif key == 'RE':
            metric = get_object_or_404(RequirementMetrics, pk=metric_id)
            form = RequirementForm(request.POST, instance=metric)
        elif key == 'TL':
            metric = get_object_or_404(LabMetrics, pk=metric_id)
            form = LabForm(request.POST, instance=metric)
        else:
            messages.error(request, 'No key to Functional Group found')
            return redirect('teams:teams')

        if form.is_valid():
            metric = form.save()
            if not metric.updated:
                metric.updated = True
                metric.save()

            context = context_teams(request)
            context['key'] = key
            return render(request, 'teams/teams.html', context)
        else:
            messages.error(request, 'Correct errors in the form')
            context = RequestContext(request, {
                'metric': metric,
                'form': form
            })
            return render(request, 'teams/metric_detail.html', context)
    else:
        return redirect('teams:teams')


def fetch_team_members_by_date(request):
    key = request.GET.get('key', '')
    date = request.GET.get('date', '')
    # print key, date

    data = team_personals = []
    year = date[:4]
    month = date[6:7]
    day = date[8:10]

    if key in ['QA', 'TE']:
        team_personals = TestStats.objects.filter(human_resource__functional_group__key=key,
                                                  created__year=year,
                                                  created__month=month,
                                                  created__day=day)
    elif key == 'QI':
        team_personals = InnovationStats.objects.filter(human_resource__functional_group__key=key,
                                                        created__year=year,
                                                        created__month=month,
                                                        created__day=day)
    elif key == 'RE':
        team_personals = RequirementStats.objects.filter(human_resource__functional_group__key=key,
                                                         created__year=year,
                                                         created__month=month,
                                                         created__day=day)
    elif key == 'TL':
        team_personals = LabStats.objects.filter(human_resource__functional_group__key=key,
                                                 created__year=year,
                                                 created__month=month,
                                                 created__day=day)

    for person in team_personals:
        temp = {}
        temp['staff'] = person.human_resource.user.first_name + ' ' + person.human_resource.user.last_name
        if person.updated:
            temp['updated'] = person.confirmed.strftime('%Y-%m-%d')
        else:
            temp['updated'] = 'Not Updated'

        data.append(temp)

    return HttpResponse(json.dumps(data), content_type="application/json")


@csrf_exempt
def add_product_quality_chart(request):
    return HttpResponse('')

@csrf_exempt
def delete_product_quality_chart(request):
    return HttpResponse('')

@csrf_exempt
def add_quality_assurance_chart(request):
    return HttpResponse('')

@csrf_exempt
def delete_quality_assurance_chart(request):
    return HttpResponse('')

@csrf_exempt
def add_quality_innovation_chart(request):
    return HttpResponse('')

@csrf_exempt
def delete_quality_innovation_chart(request):
    return HttpResponse('')

@csrf_exempt
def add_requirements_engineering_chart(request):
    return HttpResponse('')

@csrf_exempt
def delete_requirements_engineering_chart(request):
    return HttpResponse('')

@csrf_exempt
def add_test_engineering_chart(request):
    return HttpResponse('')

@csrf_exempt
def delete_test_engineering_chart(request):
    return HttpResponse('')

@csrf_exempt
def add_test_lab_chart(request):
    return HttpResponse('')

@csrf_exempt
def delete_test_lab_chart(request):
    return HttpResponse('')
