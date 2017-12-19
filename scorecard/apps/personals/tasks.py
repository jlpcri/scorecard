from datetime import date, timedelta

from django.utils import timezone

from models import InnovationStats, LabStats, RequirementStats, TestStats
from scorecard.apps.users.models import FunctionalGroup
from scorecard.celery_module import app


@app.task
def weekly_personal_stats_new():
    now = timezone.now()
    if now.isoweekday() == 1:
        this_friday = now + timedelta(days=5-now.isoweekday())
        try:
            qi = InnovationStats.objects.latest('created')
            if qi.created.date() == this_friday.date():
                err_message = 'Personal Status is already exist'

                return {
                    'valid': False,
                    'message': err_message
                }
            else:
                personal_stats_new(this_friday)
                return {
                    'valid': True
                }
        except InnovationStats.DoesNotExist:
            personal_stats_new(this_friday)
            return {
                'valid': True
            }
    else:
        err_message = 'Today is not Monday'

        return {
            'valid': False,
            'message': err_message
        }


def personal_stats_new(created):
    functional_groups = FunctionalGroup.objects.all()
    for functional_group in functional_groups:
        if functional_group.abbreviation in ['QA', 'TE']:
            hrs = functional_group.humanresource_set.all()
            for hr in hrs:
                TestStats.objects.create(human_resource=hr,
                                         created=created)
        elif functional_group.abbreviation == 'QE':
            hrs = functional_group.humanresource_set.all()
            for hr in hrs:
                InnovationStats.objects.create(human_resource=hr,
                                               created=created)
        elif functional_group.abbreviation == 'RE':
            hrs = functional_group.humanresource_set.all()
            for hr in hrs:
                RequirementStats.objects.create(human_resource=hr,
                                                created=created)
        elif functional_group.abbreviation == 'TL':
            hrs = functional_group.humanresource_set.all()
            for hr in hrs:
                LabStats.objects.create(human_resource=hr,
                                        created=created)
