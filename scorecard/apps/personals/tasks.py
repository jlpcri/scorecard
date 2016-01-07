from datetime import date, datetime

from scorecard.celery_module import app
from scorecard.apps.users.models import FunctionalGroup
from models import InnovationStats, LabStats, RequirementStats, TestStats


@app.task
def weekly_personal_stats_new():
    today = date.today()
    if today.isoweekday() == 5:
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
            hrs = functional_group.humanresource_set.all()
            for hr in hrs:
                TestStats.objects.create(human_resource=hr)
        elif functional_group.key == 'QI':
            hrs = functional_group.humanresource_set.all()
            for hr in hrs:
                InnovationStats.objects.create(human_resource=hr)
        elif functional_group.key == 'RE':
            hrs = functional_group.humanresource_set.all()
            for hr in hrs:
                RequirementStats.objects.create(human_resource=hr)
        elif functional_group.key == 'TL':
            hrs = functional_group.humanresource_set.all()
            for hr in hrs:
                LabStats.objects.create(human_resource=hr)
