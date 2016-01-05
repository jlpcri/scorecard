from datetime import date, datetime

from scorecard.celery_module import app
from scorecard.apps.users.models import FunctionalGroup, HumanResource
from models import InnovationStats, LabStats, RequirementStats, TestStats
from scorecard.apps.datas.utils import get_week_ending_date


@app.task
def weekly_personal_stats_new():
    today = date.today()
    if today.isoweekday() == 2:
        try:
            qi = InnovationStats.objects.latest('created')
            if qi.created.date() == today:
                err_message = 'Personal Status is already exist'

                return {
                    'valid': False,
                    'message': err_message
                }
            else:
                personal_stats_new()
                return {
                    'valid': True
                }
        except InnovationStats.DoesNotExist:
            personal_stats_new()
            return {
                'valid': True
            }
    else:
        err_message = 'Today is not Friday'

        return {
            'valid': False,
            'message': err_message
        }


def personal_stats_new():
    functional_groups = FunctionalGroup.objects.all()
    for functional_group in functional_groups:
        if functional_group.key in ['PQ', 'QA', 'TE']:
            print functional_group.key
        elif functional_group.key == 'QI':
            hrs = functional_group.humanresource_set.all()
            for hr in hrs:
                print hr.user.username
        elif functional_group.key == 'RE':
            print functional_group.key
        elif functional_group.key == 'TL':
            print functional_group.key
