from datetime import datetime, timedelta
from django.conf import settings
from pytz import timezone
from scorecard.apps.users.models import FunctionalGroup


def context_teams(request):
    start_end = get_start_end_from_request(request)
    start = start_end['start']
    end = start_end['end']
    qas = qis = res = tes = tls = []

    functional_groups = FunctionalGroup.objects.all()
    for functional_group in functional_groups:
        if functional_group.key == 'QA':
            qas = functional_group.testmetrics_set.filter(created__range=(start, end)).order_by('-created')
        elif functional_group.key == 'QI':
            qis = functional_group.innovationmetrics_set.filter(created__range=(start, end)).order_by('-created')
        elif functional_group.key == 'RE':
            res = functional_group.requirementmetrics_set.filter(created__range=(start, end)).order_by('-created')
        elif functional_group.key == 'TE':
            tes = functional_group.testmetrics_set.filter(created__range=(start, end)).order_by('-created')
        elif functional_group.key == 'TL':
            tls = functional_group.labmetrics_set.filter(created__range=(start, end)).order_by('-created')

    context = {
        'qas': qas,
        'qis': qis,
        'res': res,
        'tes': tes,
        'tls': tls,

        'start': start,
        'end': end
    }

    return context


def get_start_end_from_request(request):
    try:
        end = datetime.strptime(request.GET.get('end'), '%Y-%m-%d') + timedelta(seconds=24 * 60 * 60 -1)
    except (TypeError, ValueError):
        end = datetime.now()

    try:
        start = datetime.strptime(request.GET.get('start'), '%Y-%m-%d')
    except (TypeError, ValueError):
        start = end - timedelta(days=60)

    start = timezone(settings.TIME_ZONE).localize(start)
    end = timezone(settings.TIME_ZONE).localize(end)

    return {
        'start': start,
        'end': end
    }