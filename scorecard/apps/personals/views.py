from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from scorecard.apps.personals.tasks import weekly_personal_stats_new
from scorecard.apps.users.models import FunctionalGroup, HumanResource
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
    current_user_personals = []

    for function_group in function_groups:
        if function_group.key == 'PQ':
            pq = TestStats.objects.latest('created')
            pq_personals = TestStats.objects.filter(human_resource__functional_group__key='PQ',
                                                    created__year=pq.created.year,
                                                    created__month=pq.created.month,
                                                    created__day=pq.created.day)
        elif function_group.key == 'QA':
            qa = TestStats.objects.latest('created')
            qa_personals = TestStats.objects.filter(human_resource__functional_group__key='QA',
                                                    created__year=qa.created.year,
                                                    created__month=qa.created.month,
                                                    created__day=qa.created.day)
        elif function_group.key == 'TE':
            te = TestStats.objects.latest('created')
            te_personals = TestStats.objects.filter(human_resource__functional_group__key='TE',
                                                    created__year=te.created.year,
                                                    created__month=te.created.month,
                                                    created__day=te.created.day)
        elif function_group.key == 'QI':
            # hrs = function_group.humanresource_set.all()
            # for hr in hrs:
            #     qi_personals += hr.innovationstats_set.all()
            qi = InnovationStats.objects.latest('created')
            qi_personals = InnovationStats.objects.filter(created__year=qi.created.year,
                                                          created__month=qi.created.month,
                                                          created__day=qi.created.day)
        elif function_group.key == 'RE':
            re = RequirementStats.objects.latest('created')
            re_personals = RequirementStats.objects.filter(created__year=re.created.year,
                                                           created__month=re.created.month,
                                                           created__day=re.created.day)
        elif function_group.key == 'TL':
            tl = LabStats.objects.latest('created')
            tl_personals = LabStats.objects.filter(created__year=tl.created.year,
                                                   created__month=tl.created.month,
                                                   created__day=tl.created.day)

    hr = HumanResource.objects.get(user=request.user)
    if hr.functional_group:
        if hr.functional_group.key in ['PQ', 'QA', 'TE']:
            current_user_personals = hr.teststats_set.all()
        elif hr.functional_group.key == 'QI':
            current_user_personals = hr.innovationstats_set.all()
        elif hr.functional_group.key == 'RE':
            current_user_personals = hr.requirementstats_set.all()
        elif hr.functional_group.key == 'TL':
            current_user_personals = hr.labstats_set.all()

    context = RequestContext(request, {
        'pq_personals': pq_personals,
        'qa_personals': qa_personals,
        'te_personals': te_personals,
        'qi_personals': qi_personals,
        're_personals': re_personals,
        'tl_personals': tl_personals,
        'current_user_personals': current_user_personals
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


@login_required
def personal_stats(request, stats_id):
    key = request.GET.get('key', '')
    print key