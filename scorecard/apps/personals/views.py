from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import RequestContext

from scorecard.apps.users.models import FunctionalGroup


@login_required
def personals(request):
    function_groups = FunctionalGroup.objects.all()
    pq_individuals = []
    qa_individuals = []
    te_individuals = []

    # for function_group in function_groups:
    #     if function_group.key == 'PQ':
    #         hrs = function_group.humanresource_set.all()
    #         for hr in hrs:
    #             pq_individuals += hr.productqualityindividual_set.all()
    #     elif function_group.key == 'QA':
    #         hrs = function_group.humanresource_set.all()
    #         for hr in hrs:
    #             qa_individuals += hr.qualityassuranceindividual_set.all()
    #     elif function_group.key == 'TE':
    #         hrs = function_group.humanresource_set.all()
    #         for hr in hrs:
    #             te_individuals += hr.testengineeringindividual_set.all()

    context = RequestContext(request, {
        'pq_individuals': pq_individuals,
        'qa_individuals': qa_individuals,
        'te_individuals': te_individuals
    })

    return render(request, 'personals/personals.html', context)
