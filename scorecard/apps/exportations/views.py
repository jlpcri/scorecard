from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import RequestContext

from scorecard.apps.users.models import FunctionalGroup
from scorecard.apps.teams.models import InnovationMetrics


@login_required
def exportations(request):
    functional_groups = FunctionalGroup.objects.all().order_by('name')
    data = {}
    data_name = []
    data_key = []
    for functional_group in functional_groups:
        data_name.append(functional_group.name)
        data_key.append(functional_group.key)

    dates = InnovationMetrics.objects.values_list('created', flat=True)
    data['name'] = data_name
    data['key'] = data_key
    data['dates'] = dates

    context = RequestContext(request, {
        'data': data
    })

    return render(request, 'exportations/exportations.html', context)

