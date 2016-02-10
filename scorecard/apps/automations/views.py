from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template import RequestContext

from models import Automation
from forms import AutomationNewForm
from scorecard.apps.users.models import FunctionalGroup


@login_required
def automations(request):
    qas = qis = res = tes = tls = []
    functional_groups = FunctionalGroup.objects.all()
    for fg in functional_groups:
        if fg.key == 'QA':
            qas = fg.automation_set.order_by('column_field')
        elif fg.key == 'QI':
            qis = fg.automation_set.order_by('column_field')
        elif fg.key == 'RE':
            res = fg.automation_set.order_by('column_field')
        elif fg.key == 'TE':
            tes = fg.automation_set.order_by('column_field')
        elif fg.key == 'TL':
            tls = fg.automation_set.order_by('column_field')

    automation_new_form = AutomationNewForm()

    context = RequestContext(request, {
        'qas': qas,
        'qis': qis,
        'res': res,
        'tes': tes,
        'tls': tls,

        'form': automation_new_form
    })
    return render(request, 'automations/automations.html', context)


def automation_detail(request, automation_id):
    pass


def automation_edit(request, automation_id):
    pass


def automation_new(request):
    if request.method == 'POST':
        form = AutomationNewForm(request.POST)
        if form.is_valid():
            automation = form.save()
            messages.success(request, 'Project is added')
        else:
            messages.error(request, 'Errors found')

        return redirect('automations:automations')
