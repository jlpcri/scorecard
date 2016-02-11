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
            # automation_new_form = AutomationNewForm(initial={'key': fg.key})
        elif fg.key == 'RE':
            res = fg.automation_set.order_by('column_field')
        elif fg.key == 'TE':
            tes = fg.automation_set.order_by('column_field')
        elif fg.key == 'TL':
            tls = fg.automation_set.order_by('column_field')

    automation_new_form = AutomationNewForm(initial={'functional_group': request.user.humanresource.functional_group,
                                                     'key': request.user.humanresource.functional_group.key})

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
        form = AutomationNewForm(request.POST, request.FILES, initial={'key': request.user.humanresource.functional_group.key})
        if form.is_valid():
            automation = form.save()
            if not form.cleaned_data['script_name'] and request.FILES['script_file']:
                automation.script_name = request.FILES['script_file'].name
                automation.save()

            messages.success(request, 'Project is added')
        else:
            print form.errors
            messages.error(request, 'Errors found')

        return redirect('automations:automations')
