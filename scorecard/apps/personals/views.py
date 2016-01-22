import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext

from scorecard.apps.personals.tasks import weekly_personal_stats_new
from scorecard.apps.personals.utils import get_distinct_dates
from scorecard.apps.users.models import FunctionalGroup, HumanResource
from models import InnovationStats, LabStats, RequirementStats, TestStats
from scorecard.apps.users.views import user_is_superuser
from forms import InnovationForm, LabForm, RequirementForm, TestForm


@login_required
def personals(request):
    function_groups = FunctionalGroup.objects.all()
    qa_personals = []
    te_personals = []
    qi_personals = []
    re_personals = []
    tl_personals = []
    current_user_personals = []

    for function_group in function_groups:
        if function_group.key == 'QA':
            try:
                qa = TestStats.objects.latest('created')
                qa_personals = TestStats.objects.filter(human_resource__functional_group__key='QA',
                                                        created__year=qa.created.year,
                                                        created__month=qa.created.month,
                                                        created__day=qa.created.day)
            except TestStats.DoesNotExist:
                pass
        elif function_group.key == 'TE':
            try:
                te = TestStats.objects.latest('created')
                te_personals = TestStats.objects.filter(human_resource__functional_group__key='TE',
                                                        created__year=te.created.year,
                                                        created__month=te.created.month,
                                                        created__day=te.created.day)
            except TestStats.DoesNotExist:
                pass
        elif function_group.key == 'QI':
            try:
                qi = InnovationStats.objects.latest('created')
                qi_personals = InnovationStats.objects.filter(created__year=qi.created.year,
                                                              created__month=qi.created.month,
                                                              created__day=qi.created.day)
            except InnovationStats.DoesNotExist:
                pass
        elif function_group.key == 'RE':
            try:
                re = RequirementStats.objects.latest('created')
                re_personals = RequirementStats.objects.filter(created__year=re.created.year,
                                                               created__month=re.created.month,
                                                               created__day=re.created.day)
            except RequirementStats.DoesNotExist:
                pass
        elif function_group.key == 'TL':
            try:
                tl = LabStats.objects.latest('created')
                tl_personals = LabStats.objects.filter(created__year=tl.created.year,
                                                       created__month=tl.created.month,
                                                       created__day=tl.created.day)
            except LabStats.DoesNotExist:
                pass

    hr = HumanResource.objects.get(user=request.user)
    if hr.functional_group:
        if hr.functional_group.key in ['QA', 'TE']:
            current_user_personals = hr.teststats_set.all()
        elif hr.functional_group.key == 'QI':
            current_user_personals = hr.innovationstats_set.all()
        elif hr.functional_group.key == 'RE':
            current_user_personals = hr.requirementstats_set.all()
        elif hr.functional_group.key == 'TL':
            current_user_personals = hr.labstats_set.all()

    dates = get_distinct_dates()

    context = RequestContext(request, {
        'qa_personals': qa_personals,
        'te_personals': te_personals,
        'qi_personals': qi_personals,
        're_personals': re_personals,
        'tl_personals': tl_personals,

        'current_user_personals': current_user_personals,
        'dates': dates
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

    if key in ['QA', 'TE']:
        personal_stat = get_object_or_404(TestStats, pk=stats_id)
        form = TestForm(instance=personal_stat)
    elif key == 'QI':
        personal_stat = get_object_or_404(InnovationStats, pk=stats_id)
        form = InnovationForm(instance=personal_stat)
    elif key == 'RE':
        personal_stat = get_object_or_404(RequirementStats, pk=stats_id)
        form = RequirementForm(instance=personal_stat)
    elif key == 'TL':
        personal_stat = get_object_or_404(LabStats, pk=stats_id)
        form = LabForm(instance=personal_stat)
    else:
        messages.error(request, 'No key to Human Resource found')
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
    for functional_gruop in functional_groups:
        if functional_gruop.key == 'QA':
            qa_personals = fetch_personals_per_team_per_date(functional_gruop.key, date)
        elif functional_gruop.key == 'TE':
            te_personals = fetch_personals_per_team_per_date(functional_gruop.key, date)
        elif functional_gruop.key == 'QI':
            qi_personals = fetch_personals_per_team_per_date(functional_gruop.key, date)
        elif functional_gruop.key == 'RE':
            re_personals = fetch_personals_per_team_per_date(functional_gruop.key, date)
        elif functional_gruop.key == 'TL':
            tl_personals = fetch_personals_per_team_per_date(functional_gruop.key, date)

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

