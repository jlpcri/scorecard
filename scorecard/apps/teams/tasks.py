import socket
from datetime import datetime, timedelta

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone

from models import (InnovationMetrics, LabMetrics, RequirementMetrics,
                    TestMetrics)
from scorecard.apps.datas.utils import get_week_ending_date
from scorecard.apps.users.models import FunctionalGroup
from scorecard.celery_module import app


@app.task
def weekly_metric_new():
    now = timezone.now()
    if now.isoweekday() == 1:
        this_friday = now + timedelta(days=5-now.isoweekday())
        try:
            qi = InnovationMetrics.objects.latest('created')
            if qi.created.date() == this_friday.date():
                err_message = 'Metric is already exist'
                err_message_send_email(err_message)

                return {
                    'valid': False,
                    'message': err_message
                }
            else:
                metric_new(this_friday)
                return {
                    'valid': True
                }
        except InnovationMetrics.DoesNotExist:
            metric_new(this_friday)
            return {
                'valid': True
            }
    else:
        err_message = 'Today is not Monday'
        err_message_send_email(err_message)

        return {
            'valid': False,
            'message': err_message
        }


def metric_new(created):
    functional_groups = FunctionalGroup.objects.all()
    for functional_group in functional_groups:
        if functional_group.abbreviation == 'QA':
            for subteam in functional_group.subteam_set.exclude(name='Legacy'):
                TestMetrics.objects.create(functional_group=functional_group,
                                           subteam=subteam,
                                           created=created)
            TestMetrics.objects.create(functional_group=functional_group,
                                       created=created)  # Team entry
        elif functional_group.abbreviation == 'TE':
            for subteam in functional_group.subteam_set.exclude(name='Legacy'):
                TestMetrics.objects.create(functional_group=functional_group,
                                           subteam=subteam,
                                           created=created)
            TestMetrics.objects.create(functional_group=functional_group,
                                       created=created)  # Team entry
        elif functional_group.abbreviation == 'QE':
            for subteam in functional_group.subteam_set.all():
                InnovationMetrics.objects.create(functional_group=functional_group,
                                                 subteam=subteam,
                                                 created=created)
            InnovationMetrics.objects.create(functional_group=functional_group,
                                             created=created)  # Team Entry

        elif functional_group.abbreviation == 'RE':
            for subteam in functional_group.subteam_set.all():
                RequirementMetrics.objects.create(functional_group=functional_group,
                                                  subteam=subteam,
                                                  created=created)
            RequirementMetrics.objects.create(functional_group=functional_group,
                                              created=created)  # Team Entry
        elif functional_group.abbreviation == 'TL':
            for subteam in functional_group.subteam_set.all():
                LabMetrics.objects.create(functional_group=functional_group,
                                          subteam=subteam,
                                          created=created)
            LabMetrics.objects.create(functional_group=functional_group,
                                      created=created)  # Team Entry

    weekly_send_email()


def weekly_send_email():

    today = datetime.today()
    today_weekday = today.isoweekday()
    if today_weekday != 5:
        this_friday = today + timedelta(days=5-today_weekday)
    else:
        this_friday = today
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
    to_email = ['sliu@west.com', 'QEIInnovation@west.com'] + managers_email
    # to_email = ['sliu@west.com']
    content = '<p>Following are the links to access the week <strong>{0}</strong> Scorecard manager input:</p>'.format(get_week_ending_date(this_friday))
    content += '<ul>'

    for functional_group in functional_groups:
        if functional_group.abbreviation == 'QE':
            metric = InnovationMetrics.objects.latest('created')
            content += '<li><a href=\'{0}teams/metric_detail/{1}/?key={2}\'>{3}</a></li>'.format(settings.HOST_URL, metric.id, functional_group.abbreviation, functional_group.name)

        elif functional_group.abbreviation == 'RE':
            metric = RequirementMetrics.objects.latest('created')
            content += '<li><a href=\'{0}teams/metric_detail/{1}/?key={2}\'>{3}</a></li>'.format(settings.HOST_URL, metric.id, functional_group.abbreviation, functional_group.name)

        elif functional_group.abbreviation == 'TL':
            metric = LabMetrics.objects.latest('created')
            content += '<li><a href=\'{0}teams/metric_detail/{1}/?key={2}\'>{3}</a></li>'.format(settings.HOST_URL, metric.id, functional_group.abbreviation, functional_group.name)

        elif functional_group.abbreviation in ['QA', 'TE']:
            content += '<li>{0}</li><ul>'.format(functional_group.name)
            for subteam in functional_group.subteam_set.exclude(name='Legacy'):
                metric = TestMetrics.objects.filter(subteam=subteam).latest('created')
                content += '<li><a href=\'{0}teams/metric_detail/{1}/?key={2}\'>{3}</a></li>'.format(settings.HOST_URL, metric.id, functional_group.abbreviation, subteam.name)
            content += '</ul>'

    content += '</ul>'

    msg = EmailMultiAlternatives(subject, content, from_email, to_email)
    msg.content_subtype = 'html'

    msg.send()


def err_message_send_email(err_message):
    subject = 'Add New Metric Error'
    from_email = 'QEIInnovation@west.com'

    to_email = ['sliu@west.com']
    content = '<h4>{0}</h4>'.format(err_message)

    msg = EmailMultiAlternatives(subject, content, from_email, to_email)
    msg.content_subtype = 'html'

    msg.send()
