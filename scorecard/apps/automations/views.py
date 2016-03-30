import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext

from models import Automation
from forms import AutomationNewForm, AutomationForm
from scorecard.apps.users.models import FunctionalGroup, Subteam


@login_required
def automations(request):
    groups = []
    functional_groups = FunctionalGroup.objects.all()
    for group in functional_groups:
        group_dict = {
            'group': group,
            'subteams': [{
                'team': team,
                'columns': team.automation_set.order_by('column_field')
            }
             for team in Subteam.objects.filter(parent=group).exclude(name='Legacy')]
        }
        groups.append(group_dict)

    try:
        automation_new_form = AutomationNewForm(initial={'subteam': request.user.humanresource.subteam,
                                                         'abbreviation': request.user.humanresource.functional_group.abbreviation})

    except AttributeError as e:
        print e.message, type(e)
        automation_new_form = AutomationNewForm(initial={'subteam': Subteam.objects.filter(parent__abbreviation='QA'),
                                                         'abbreviation': 'QA'})

    personals = request.user.humanresource.automation_set.order_by('column_field')
    context = RequestContext(request, {
        'groups': groups,
        'form': automation_new_form,
        'personals': personals
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
        form = AutomationNewForm(request.POST, request.FILES, initial={'abbreviation': request.user.humanresource.functional_group.abbreviation})
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