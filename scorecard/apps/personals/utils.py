from datetime import date, timedelta
from itertools import groupby

from models import InnovationStats, TestStats, RequirementStats, LabStats
from scorecard.apps.users.models import FunctionalGroup, HumanResource
from scorecard.apps.datas.utils import get_week_ending_date


def get_distinct_dates():
    result = []
    qis = InnovationStats.objects.order_by('-created')
    for created_date, group in groupby(qis, key=extract_date):
        result.append(created_date)

    return result


def extract_date(qi):
    return get_week_ending_date(qi.created)


def check_new_login_on_friday():
    today = date.today()
    last_friday = today - timedelta(days=today.isoweekday() + 2)
    print today, last_friday
    if today.isoweekday() == 5:
        for fg in FunctionalGroup.objects.all():
            check_new_login_on_friday_per_team(fg.key, last_friday)
    else:
        print 'Not Friday'


def check_new_login_on_friday_per_team(key, today):
    hrs = HumanResource.objects.filter(functional_group__key=key)
    personals = []
    # today = date.today()
    if key in ['QA', 'TE']:
        personals = TestStats.objects.filter(human_resource__functional_group__key=key,
                                             created__year=today.year,
                                             created__month=today.month,
                                             created__day=today.day)
    elif key == 'QI':
        personals = InnovationStats.objects.filter(human_resource__functional_group__key=key,
                                                   created__year=today.year,
                                                   created__month=today.month,
                                                   created__day=today.day)
    elif key == 'RE':
        personals = RequirementStats.objects.filter(human_resource__functional_group__key=key,
                                                    created__year=today.year,
                                                    created__month=today.month,
                                                    created__day=today.day)
    elif key == 'TL':
        personals = LabStats.objects.filter(human_resource__functional_group__key=key,
                                            created__year=today.year,
                                            created__month=today.month,
                                            created__day=today.day)

    hrs_users = hrs.values_list('user__username', flat=True)
    personals_users = personals.values_list('human_resource__user__username', flat=True)
    print key, list(set(hrs_users) - set(personals_users))
