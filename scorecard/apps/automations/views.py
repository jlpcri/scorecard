from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import RequestContext

from models import InnovationAutomation, LabAutomation, RequirementAutomation, TestAutomation
from scorecard.apps.users.models import FunctionalGroup


@login_required
def automations(request):
    qas = qis = res = tes = tls = []
    functional_groups = FunctionalGroup.objects.all()
    for fg in functional_groups:
        if fg.key == 'QA':
            qas = fg.testautomation_set.order_by('column_field')
        elif fg.key == 'QI':
            qis = fg.innovationautomation_set.order_by('column_field')
        elif fg.key == 'RE':
            res = fg.requirementautomation_set.order_by('column_field')
        elif fg.key == 'TE':
            tes = fg.testautomation_set.order_by('column_field')
        elif fg.key == 'TL':
            tls = fg.labautomation_set.order_by('column_field')

    context = RequestContext(request, {
        'qas': qas,
        'qis': qis,
        'res': res,
        'tes': tes,
        'tls': tls
    })
    return render(request, 'automations/automations.html', context)


def automation_detail(request, automation_id):
    pass


def automation_edit(request, automation_id):
    pass


def automation_new(request):
    pass
