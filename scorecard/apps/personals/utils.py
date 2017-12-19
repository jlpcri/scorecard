from datetime import date, timedelta
from itertools import groupby

from models import InnovationStats, LabStats, RequirementStats, TestStats
from scorecard.apps.automations.models import Automation
from scorecard.apps.automations.utils import get_model_fields
from scorecard.apps.datas.utils import get_week_ending_date


def get_distinct_dates():
    result = []
    qis = InnovationStats.objects.order_by('-created')
    for created_date, group in groupby(qis, key=extract_date):
        result.append(created_date)

    return result


def extract_date(qi):
    return get_week_ending_date(qi.created)


def get_automation_data(request, personal_stat):
    data = {}
    level = 'person'
    key = personal_stat.human_resource.functional_group.abbreviation
    date = personal_stat.created.strftime('%Y-%m-%d')

    if key == 'QE':
        choices = get_model_fields(InnovationStats, key, level)
    elif key == 'TL':
        choices = get_model_fields(LabStats, key, level)
    elif key == 'RE':
        choices = get_model_fields(RequirementStats, key, level)
    else:
        choices = get_model_fields(TestStats, key, level)

    for item in choices:
        try:
            automation = Automation.objects.get(human_resource=personal_stat.human_resource,
                                                column_field=item[0])
            if automation.script_file:
                try:
                    exec(automation.script_file.read())
                except IOError:
                    continue

                try:
                    result = run_script(date, automation.human_resource.user.username)
                except Exception:
                    result = 0

                data[item[0]] = result
        except Automation.DoesNotExist:
            continue

    return data
