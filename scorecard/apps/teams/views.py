from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import RequestContext

from models import  TestMetrics, RequirementMetrics, InnovationMetrics, LabMetrics


@login_required
def teams(request):
    qis = InnovationMetrics.objects.all()
    tls = LabMetrics.objects.all()
    res = RequirementMetrics.objects.all()

    pqs = TestMetrics.objects.filter(functional_group__key='PQ')
    qas = TestMetrics.objects.filter(functional_group__key='QA')
    tes = TestMetrics.objects.filter(functional_group__key='TE')

    context = RequestContext(request, {
        'pqs': pqs,
        'qas': qas,
        'qis': qis,
        'res': res,
        'tes': tes,
        'tls': tls
    })
    return render(request, 'teams/teams.html', context)

