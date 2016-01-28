from datetime import datetime, timedelta
from django.conf import settings
from pytz import timezone
from scorecard.apps.personals.models import TestStats, RequirementStats, LabStats
from scorecard.apps.personals.models import InnovationStats
from scorecard.apps.users.models import FunctionalGroup


def context_teams(request):
    start_end = get_start_end_from_request(request)
    start = start_end['start']
    end = start_end['end']
    qas = qis = res = tes = tls = []

    functional_groups = FunctionalGroup.objects.all()
    for functional_group in functional_groups:
        if functional_group.key == 'QA':
            qas = functional_group.testmetrics_set.filter(created__range=(start, end)).order_by('-created')
        elif functional_group.key == 'QI':
            qis = functional_group.innovationmetrics_set.filter(created__range=(start, end)).order_by('-created')
        elif functional_group.key == 'RE':
            res = functional_group.requirementmetrics_set.filter(created__range=(start, end)).order_by('-created')
        elif functional_group.key == 'TE':
            tes = functional_group.testmetrics_set.filter(created__range=(start, end)).order_by('-created')
        elif functional_group.key == 'TL':
            tls = functional_group.labmetrics_set.filter(created__range=(start, end)).order_by('-created')

    context = {
        'qas': qas,
        'qis': qis,
        'res': res,
        'tes': tes,
        'tls': tls,

        'start': start,
        'end': end
    }

    return context


def get_start_end_from_request(request):
    try:
        end = datetime.strptime(request.GET.get('end'), '%Y-%m-%d') + timedelta(seconds=24 * 60 * 60 -1)
    except (TypeError, ValueError):
        end = datetime.now()

    try:
        start = datetime.strptime(request.GET.get('start'), '%Y-%m-%d')
    except (TypeError, ValueError):
        start = end - timedelta(days=60)

    start = timezone(settings.TIME_ZONE).localize(start)
    end = timezone(settings.TIME_ZONE).localize(end)

    return {
        'start': start,
        'end': end
    }


def fetch_team_members_per_team_per_date(key, date):
    year = date[:4]
    month = date[6:7]
    day = date[8:10]
    team_personals = []

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

    return team_personals


def fetch_collect_data_per_team_per_date(key, date):
    data = {}
    team_personals = fetch_team_members_per_team_per_date(key, date)

    overtime_weekday = overtime_weekend = rework_time = 0
    tc_manual_dev = tc_manual_dev_time = tc_manual_execution = tc_manual_execution_time = 0
    tc_auto_dev = tc_auto_dev_time = tc_auto_execution = tc_auto_execution_time = 0
    defect_caught = uat_defects_not_prevented = standards_violated = resource_swap_time = 0

    if key in ['QA', 'TE']:
        for person in team_personals:
            overtime_weekday += person.overtime_weekday
            overtime_weekend += person.overtime_weekend
            rework_time += person.rework_time

            tc_manual_dev += person.tc_manual_dev
            tc_manual_dev_time += person.tc_manual_dev_time
            tc_manual_execution += person.tc_manual_execution
            tc_manual_execution_time += person.tc_manual_execution_time

            tc_auto_dev += person.tc_auto_dev
            tc_auto_dev_time += person.tc_auto_dev_time
            tc_auto_execution += person.tc_auto_execution
            tc_auto_execution_time += person.tc_auto_execution_time

            defect_caught += person.defect_caught
            uat_defects_not_prevented += person.uat_defects_not_prevented
            standards_violated += person.standards_violated
            resource_swap_time += person.resource_swap_time

        data = {
            'overtime_weekday': overtime_weekday,
            'overtime_weekend': overtime_weekend,
            'rework_time': rework_time,
            'tc_manual_dev': tc_manual_dev,
            'tc_manual_dev_time': tc_manual_dev_time,
            'tc_manual_execution': tc_auto_execution,
            'tc_manual_execution_time': tc_manual_execution_time,
            'tc_auto_dev': tc_auto_dev,
            'tc_auto_dev_time': tc_auto_dev_time,
            'tc_auto_execution': tc_auto_execution,
            'tc_auto_execution_time': tc_auto_execution_time,
            'defect_caught': defect_caught,
            'uat_defects_not_prevented': uat_defects_not_prevented,
            'standards_violated': standards_violated,
            'resource_swap_time': resource_swap_time
        }

    elif key == 'QI':
        pass
    elif key == 'RE':
        pass
    elif key == 'TL':
        pass

    return data
