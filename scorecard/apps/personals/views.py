import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from scorecard.apps.core.views import check_user_team

from scorecard.apps.personals.tasks import weekly_personal_stats_new
from scorecard.apps.personals.utils import get_distinct_dates
from scorecard.apps.users.models import FunctionalGroup, HumanResource
from models import InnovationStats, LabStats, RequirementStats, TestStats
from scorecard.apps.users.views import user_is_superuser
from forms import InnovationForm, LabForm, RequirementForm, TestForm


@login_required
def personals(request):
    check_user_team(request)
    if not (request.user.is_superuser or request.user.humanresource.manager):
        return render(request, 'personals/nonmanager.html', {'stats': request.user.humanresource.stat_set.all().order_by('-created')})
    if request.GET.get('expand', None) and (request.user.is_superuser or request.user.humanresource.manager):
        return render(request, 'personals/nonmanager.html', {'stats': HumanResource.objects.get(id=request.GET.get('expand', None)).stat_set.all().order_by('-created')})

    function_groups = FunctionalGroup.objects.all().order_by('name')
    dates = get_distinct_dates()
    context = RequestContext(request, {
        'groups': function_groups,
        'dates': dates,
    })

    return render(request, 'personals/personals.html', context)


@login_required
@user_passes_test(user_is_superuser)
def weekly_personal_stats_new_manually(request):
    """
    :param request:
    :return: result valid or error
    """

    result = weekly_personal_stats_new()
    if not result['valid']:
        messages.error(request, result['message'])

    return HttpResponseRedirect(reverse('personals:personals'))


@login_required
def personal_stats(request, stats_id):
    key = request.GET.get('key', '')
    try:
        fg = FunctionalGroup.objects.get(abbreviation=key)
        if fg.metric_type == FunctionalGroup.TESTING:
            personal_stat = TestStats.objects.get(pk=stats_id)
            form = TestForm(instance=personal_stat)
        elif fg.metric_type == FunctionalGroup.DEVELOPMENT:
            personal_stat = InnovationStats.objects.get(pk=stats_id)
            form = InnovationForm(instance=personal_stat)
        elif fg.metric_type == FunctionalGroup.REQUIREMENTS:
            personal_stat = RequirementStats.objects.get(pk=stats_id)
            form = RequirementForm(instance=personal_stat)
        elif fg.metric_type == FunctionalGroup.LAB:
            personal_stat = LabStats.objects.get(pk=stats_id)
            form = LabForm(instance=personal_stat)
        else:
            raise ValueError("Fell through stat retrieval table")
    except Exception as e:
        print e
        messages.error(request, 'Failed to load selected scorecard. Please email QEIInnovation@west.com for assistance.')
        return redirect('personals:personals')

    context = RequestContext(request, {
        'personal_stat': personal_stat,
        'form': form
    })

    return render(request, 'personals/personal_stats.html', context)


@login_required
def personal_stats_edit(request, stats_id):
    key = request.GET.get('key', '')

    if request.method == 'POST':
        if key in ['QA', 'TE']:
            personal_stat = get_object_or_404(TestStats, pk=stats_id)
            form = TestForm(request.POST, instance=personal_stat)
        elif key == 'QI':
            personal_stat = get_object_or_404(InnovationStats, pk=stats_id)
            form = InnovationForm(request.POST, instance=personal_stat)
        elif key == 'RE':
            personal_stat = get_object_or_404(RequirementStats, pk=stats_id)
            form = RequirementForm(request.POST, instance=personal_stat)
        elif key == 'TL':
            personal_stat = get_object_or_404(LabStats, pk=stats_id)
            form = LabForm(request.POST, instance=personal_stat)

        if form.is_valid():
            personal_stat = form.save()
            if not personal_stat.updated:
                personal_stat.updated = True
                personal_stat.save()

            return redirect('personals:personals')
        else:
            messages.error(request, 'Correct errors in the form')
            context = RequestContext(request, {
                'personal_stat': personal_stat,
                'form': form
            })
            return render(request, 'personals/personal_stats.html', context)
    else:
        return redirect('personals:personals')


def fetch_personals_by_date(request):
    date = request.GET.get('date', '')

    data = {}
    data['date'] = date

    qa_personals = []
    te_personals = []
    qi_personals = []
    re_personals = []
    tl_personals = []

    functional_groups = FunctionalGroup.objects.all()
    for group in functional_groups:
        if group.key == 'QA':
            qa_personals = fetch_personals_per_team_per_date(group.key, date)
        elif group.key == 'TE':
            te_personals = fetch_personals_per_team_per_date(group.key, date)
        elif group.key == 'QI':
            qi_personals = fetch_personals_per_team_per_date(group.key, date)
        elif group.key == 'RE':
            re_personals = fetch_personals_per_team_per_date(group.key, date)
        elif group.key == 'TL':
            tl_personals = fetch_personals_per_team_per_date(group.key, date)

    data['qa_personals'] = qa_personals
    data['te_personals'] = te_personals
    data['qi_personals'] = qi_personals
    data['re_personals'] = re_personals
    data['tl_personals'] = tl_personals

    return HttpResponse(json.dumps(data), content_type="application/json")


def fetch_personals_per_team_per_date(key, date):
    year = date[:4]
    month = date[6:7]
    day = date[8:10]
    data = []

    if key in ['QA', 'TE']:
        team_personals = TestStats.objects.filter(human_resource__functional_group__key=key,
                                                  created__year=year,
                                                  created__month=month,
                                                  created__day=day)

        for person in team_personals:
            temp = {}
            temp['id'] = person.id
            temp['staff'] = person.human_resource.user.first_name + ' ' + person.human_resource.user.last_name
            temp['tc_manual_dev'] = str(person.tc_manual_dev)
            temp['tc_manual_exec'] = str(person.tc_manual_execution)
            temp['tc_auto_dev'] = str(person.tc_auto_dev)
            temp['tc_auto_exec'] = str(person.tc_auto_execution)

            data.append(temp)
    elif key == 'QI':
        team_personals = InnovationStats.objects.filter(created__year=year,
                                                        created__month=month,
                                                        created__day=day)
        for person in team_personals:
            temp = {}
            temp['id'] = person.id
            temp['staff'] = person.human_resource.user.first_name + ' ' + person.human_resource.user.last_name
            temp['story_points'] = str(person.story_points_execution)
            temp['unit_tests_dev'] = str(person.unit_tests_dev)
            temp['analysis_time'] = str(person.elicitation_analysis_time)

            data.append(temp)
    elif key == 'RE':
        team_personals = RequirementStats.objects.filter(created__year=year,
                                                         created__month=month,
                                                         created__day=day)
        for person in team_personals:
            temp = {}
            temp['id'] = person.id
            temp['staff'] = person.human_resource.user.first_name + ' ' + person.human_resource.user.last_name
            temp['analysis_time'] = str(person.elicitation_analysis_time)
            temp['revisions'] = str(person.revisions)
            temp['rework_internal'] = str(person.rework_time)
            temp['rework_external'] = str(person.rework_external_time)
            temp['travel_cost'] = str(person.travel_cost)

            data.append(temp)

    elif key == 'TL':
        team_personals = LabStats.objects.filter(created__year=year,
                                                 created__month=month,
                                                 created__day=day)
        for person in team_personals:
            temp = {}
            temp['id'] = person.id
            temp['staff'] = person.human_resource.user.first_name + ' ' + person.human_resource.user.last_name
            temp['tickets_closed'] = str(person.tickets_closed)
            temp['rework_time'] = str(person.rework_time)
            temp['overtime_weekday'] = str(person.overtime_weekday)

            data.append(temp)

    return data

