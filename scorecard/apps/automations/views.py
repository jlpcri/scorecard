import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext

from models import Automation
from forms import AutomationNewForm, AutomationForm
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

    try:
        automation_new_form = AutomationNewForm(initial={'functional_group': request.user.humanresource.functional_group,
                                                         'key': request.user.humanresource.functional_group.abbreviation})
    except AttributeError as e:
        # print e.message, type(e)
        automation_new_form = AutomationNewForm(initial={'functional_group': FunctionalGroup.objects.get(abbreviation='QA'),
                                                         'key': 'QA'})

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
    automation = get_object_or_404(Automation, pk=automation_id)
    form = AutomationForm(instance=automation)

    if automation.script_file:
        try:
            script_content = automation.script_file.read()
        except IOError:
            script_content = ''
    else:
        script_content = ''

    context = RequestContext(request, {
        'automation': automation,
        'form': form,
        'script_content': script_content
    })

    return render(request, 'automations/automation.html', context)


def automation_edit(request, automation_id):
    automation = get_object_or_404(Automation, pk=automation_id)
    if request.method == 'POST':
        form = AutomationForm(request.POST, request.FILES, instance=automation)
        if form.is_valid():
            if request.FILES and not request.FILES['script_file'].name.endswith('.py'):
                messages.error(request, 'Invalid file type, unable to upload (must be .py)')
                return redirect('automations:automation_detail', automation.id)

            automation = form.save()
            if not form.cleaned_data['script_name'] and request.FILES:
                automation.script_name = request.FILES['script_file'].name
                automation.save()
            messages.success(request, 'Automation is saved')
        else:
            # print form.errors
            messages.error(request, 'Errors found in Automation Edit')

        return redirect('automations:automations')


def automation_new(request):
    if request.method == 'POST':
        form = AutomationNewForm(request.POST, request.FILES, initial={'key': request.user.humanresource.functional_group.key})
        if form.is_valid():
            if request.FILES and not request.FILES['script_file'].name.endswith('.py'):
                messages.error(request, 'Invalid file type, unable to upload (must be .py)')
                return redirect('automations:automations')

            automation = form.save()
            if not form.cleaned_data['script_name'] and request.FILES:
                automation.script_name = request.FILES['script_file'].name
                automation.save()

            messages.success(request, 'Automation is added')
        else:
            print form.errors
            messages.error(request, 'Errors found in Automation New')

        return redirect('automations:automations')


def run_script(request):
    automation_id = request.GET.get('automation_id', '')
    automation = get_object_or_404(Automation, pk=automation_id)

    # execute python code read from script file of automation
    if automation.script_file:
        try:
            script_code = automation.script_file.read()
            exec(script_code)

            try:
                result = run_script()
                automation.result = result
            except Exception as e:
                print '{0}: {1}'.format(e.message, type(e))
                result = 'Errors found'

            automation.tests_run += 1
            automation.save()

            data = {
                'result': result
            }
        except IOError:
            data = {
                'result': 'Cannot read file'
            }
    else:
        data = {
            'result': 'No Script File'
        }

    return HttpResponse(json.dumps(data), content_type="application/json")