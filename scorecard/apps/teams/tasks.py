from datetime import date
from django.contrib import messages
from scorecard.celery_module import app
from scorecard.apps.users.models import FunctionalGroup
from models import TestMetrics, InnovationMetrics, RequirementMetrics, LabMetrics


@app.task
def weekly_metric_new():
    today = date.today()
    if today.isoweekday() == 5:
        try:
            qi = InnovationMetrics.objects.latest('created')
            if qi.created.date() == today:
                return {
                    'valid': False,
                    'message': 'Metric is already exist'
                }
            else:
                metric_new()
                return {
                    'valid': True
                }
        except InnovationMetrics.DoesNotExist:
            metric_new()
            return {
                'valid': True
            }
    else:
        return {
            'valid': False,
            'message': 'Today is not Friday'
        }


def metric_new():
    functional_groups = FunctionalGroup.objects.all()
    for functional_group in functional_groups:
        if functional_group.key in ['PQ', 'QA', 'TE']:
            TestMetrics.objects.create(functional_group=functional_group)
        elif functional_group.key == 'QI':
            InnovationMetrics.objects.create(functional_group=functional_group)
        elif functional_group.key == 'RE':
            RequirementMetrics.objects.create(functional_group=functional_group)
        elif functional_group.key == 'TL':
            LabMetrics.objects.create(functional_group=functional_group)
