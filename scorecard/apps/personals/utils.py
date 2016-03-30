from datetime import date, timedelta
from itertools import groupby

from models import InnovationStats, TestStats, RequirementStats, LabStats
from scorecard.apps.automations.models import Automation
from scorecard.apps.datas.utils import get_week_ending_date


def get_distinct_dates():
    result = []
    qis = InnovationStats.objects.order_by('-created')
    for created_date, group in groupby(qis, key=extract_date):
        result.append(created_date)

    return result


def extract_date(qi):
    return get_week_ending_date(qi.created)


def get_automation_data(request, date=None):
    data = {}
    key = request.user.humanresource.functional_group.abbreviation
    if key == 'QE':
        choices = InnovationStats.automation_fields()
    elif key == 'TL':
        choices = LabStats.automation_fields()
    elif key == 'RE':
        choices = RequirementStats.automation_fields()
    else:
        choices = TestStats.automation_fields()

    for item in choices:
        try:
            automation = Automation.objects.get(human_resource=request.user.humanresource,
                                                column_field=item[0])
            if automation.script_file:
                try:
                    exec(automation.script_file.read())
                except IOError:
                    continue

                try:
                    result = run_script(date)
                except Exception:
                    result = 0

                data[item[0]] = result
        except Automation.DoesNotExist:
            continue

    return data
