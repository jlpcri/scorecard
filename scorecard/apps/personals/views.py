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
    pq_personals = []
    qa_personals = []
    te_personals = []
    qi_personals = []
    re_personals = []
    tl_personals = []

    for function_group in function_groups:
        if function_group.key == 'PQ':
            hrs = function_group.humanresource_set.all()
            for hr in hrs:
                pq_personals += hr.teststats_set.all()
        elif function_group.key == 'QA':
            hrs = function_group.humanresource_set.all()
            for hr in hrs:
                qa_personals += hr.teststats_set.all()
        elif function_group.key == 'TE':
            hrs = function_group.humanresource_set.all()
            for hr in hrs:
                te_personals += hr.teststats_set.all()
        elif function_group.key == 'QI':
            hrs = function_group.humanresource_set.all()
            for hr in hrs:
                qi_personals += hr.innovationstats_set.all()
        elif function_group.key == 'RE':
            hrs = function_group.humanresource_set.all()
            for hr in hrs:
                re_personals += hr.requirementstats_set.all()
        elif function_group.key == 'TL':
            hrs = function_group.humanresource_set.all()
            for hr in hrs:
                tl_personals += hr.labstats_set.all()

    context = RequestContext(request, {
        'pq_personals': pq_personals,
        'qa_personals': qa_personals,
        'te_personals': te_personals,
        'qi_personals': qi_personals,
        're_personals': re_personals,
        'tl_personals': tl_personals,

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
