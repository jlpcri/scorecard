from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from scorecard.apps.personals.tasks import weekly_personal_stats_new
from scorecard.apps.users.models import FunctionalGroup
from models import InnovationStats, LabStats, RequirementStats, TestStats
from scorecard.apps.users.views import user_is_superuser, user_is_manager


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


@login_required
@user_passes_test(user_is_superuser)
def weekly_personal_stats_new_manually(request):
    """
    :param request:
    :return: result valid or error
    """
    result = weekly_personal_stats_new()
    if not result['valid']:
        messages.error(request, result['message'])

    return HttpResponseRedirect(reverse('personals:personals'))
