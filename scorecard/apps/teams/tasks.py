from datetime import date, datetime
from django.core.mail import send_mail, EmailMultiAlternatives

from scorecard.celery_module import app
from scorecard.apps.users.models import FunctionalGroup
from models import TestMetrics, InnovationMetrics, RequirementMetrics, LabMetrics
from scorecard.apps.exportations.utils import get_week_ending_date


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
        weekly_send_email()
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


def weekly_send_email():
    today = datetime.today()
    functional_groups = FunctionalGroup.objects.all()

    subject = 'Weekly ScoreCard Data'
    from_email = 'QEIInnovation@west.com'
    to_email = ['sliu@west.com']
    content = '<p>Following are the links to access the week <strong>{0}</strong> Scorecard manager input:</p>'.format(get_week_ending_date(today))
    content += '<ul>'
    for functional_group in functional_groups:
        content += '<li>{0}</li>'.format(functional_group.name)
    content += '</ul>'

    msg = EmailMultiAlternatives(subject, content, from_email, to_email)
    msg.content_subtype = 'html'
    msg.send()
