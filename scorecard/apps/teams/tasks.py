import socket
from datetime import date, datetime
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from scorecard.celery_module import app
from scorecard.apps.users.models import FunctionalGroup
from models import TestMetrics, InnovationMetrics, RequirementMetrics, LabMetrics
from scorecard.apps.datas.utils import get_week_ending_date


@app.task
def weekly_metric_new():
    today = date.today()
    if today.isoweekday() == 5:
        try:
            qi = InnovationMetrics.objects.latest('created')
            if qi.created.date() == today:
                err_message = 'Metric is already exist'
                err_message_send_email(err_message)

                return {
                    'valid': False,
                    'message': err_message
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
        err_message = 'Today is not Friday'
        err_message_send_email(err_message)

        return {
            'valid': False,
            'message': err_message
        }


def metric_new():
    functional_groups = FunctionalGroup.objects.all()
    for functional_group in functional_groups:
        if functional_group.key in ['QA', 'TE']:
            TestMetrics.objects.create(functional_group=functional_group)
        elif functional_group.key == 'QI':
            InnovationMetrics.objects.create(functional_group=functional_group)
        elif functional_group.key == 'RE':
            RequirementMetrics.objects.create(functional_group=functional_group)
        elif functional_group.key == 'TL':
            LabMetrics.objects.create(functional_group=functional_group)

    weekly_send_email()


def weekly_send_email():

    today = datetime.today()
    functional_groups = FunctionalGroup.objects.all()

    subject = 'Weekly ScoreCard Data'
    from_email = 'QEIInnovation@west.com'
    managers_email = [
        'gaahl3@west.com',  # Requirements: Greg Ahl
        'sdpratt@west.com',  # Product Quality: Steven Pratt
        'jmlammers@west.com',  # Test Engineering: Jon Lammers
        'pshegberg@west.com',  # QA: Peggy Hegberg
        'sdeckhart@west.com',  # QA Lead: Steve Eckhart
        'pbdalton@west.com',   # QA Lead: Phil Dalton
        'rasmith@west.com',    # TL: Richard Smith
        'pjneuberger@west.com',  # TL: Paul Neuberger
        'CAHeyden@west.com'  # QI
    ]
    # to_email = ['sliu@west.com', 'QEIInnovation@west.com'] + managers_email
    to_email = ['sliu@west.com']
    content = '<p>Following are the links to access the week <strong>{0}</strong> Scorecard manager input:</p>'.format(get_week_ending_date(today))
    content += '<ul>'

    for functional_group in functional_groups:
        if functional_group.key == 'QI':
            metric = InnovationMetrics.objects.latest('created')
        elif functional_group.key == 'RE':
            metric = RequirementMetrics.objects.latest('created')
        elif functional_group.key == 'TL':
            metric = LabMetrics.objects.latest('created')
        else:
            metric = TestMetrics.objects.filter(functional_group=functional_group).latest('created')

        content += '<li><a href=\'{0}teams/metric_detail/{1}/?key={2}\'>{3}</a></li>'.format(settings.HOST_URL, metric.id, functional_group.key, functional_group.name)

    content += '</ul>'

    msg = EmailMultiAlternatives(subject, content, from_email, to_email)
    msg.content_subtype = 'html'

    if socket.gethostname() == 'sliu-OptiPlex-GX520':
        msg.send()


def err_message_send_email(err_message):
    subject = 'Add New Metric Error'
    from_email = 'QEIInnovation@west.com'

    to_email = ['sliu@west.com']
    content = '<h4>{0}</h4>'.format(err_message)

    msg = EmailMultiAlternatives(subject, content, from_email, to_email)
    msg.content_subtype = 'html'

    if socket.gethostname() == 'sliu-OptiPlex-GX520':
        msg.send()
