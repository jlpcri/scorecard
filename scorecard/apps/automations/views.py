import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext

from models import Automation
from forms import AutomationNewForm, AutomationPersonalNewForm, AutomationForm, AutomationPersonalForm, AutomationPersonalBatchForm
from scorecard.apps.users.models import FunctionalGroup, Subteam


@login_required
def automations(request):
    groups = []
    functional_groups = FunctionalGroup.objects.all().order_by('name')
    for group in functional_groups:
        group_dict = {
            'group': group,
            'subteams': [{
                'team': team,
                'columns': team.automation_set.order_by('column_field')
            }
             for team in Subteam.objects.filter(parent=group).exclude(name='Legacy')]
        }
        if request.user.is_superuser:
            personals_all = Automation.objects.filter(human_resource__functional_group=group).order_by('column_field')
            group_dict['subteams'].append({
                'team': {'name': 'Personals'},
                'columns': personals_all
            })
        groups.append(group_dict)

    try:
        automation_new_form = AutomationNewForm(initial={
            'subteam': request.user.humanresource.subteam,
            'abbreviation': request.user.humanresource.functional_group.abbreviation})
        automation_personal_new_form = AutomationPersonalNewForm(initial={
            'human_resource': request.user.humanresource,
            'abbreviation': request.user.humanresource.functional_group.abbreviation
        })
        automation_personal_batch_form = AutomationPersonalBatchForm(initial={
            'abbreviation': request.user.humanresource.functional_group.abbreviation
        })

    except AttributeError as e:
        print e.message, type(e)
        automation_new_form = AutomationNewForm(initial={
            'subteam': Subteam.objects.filter(parent__abbreviation='QA'),
            'abbreviation': 'QA'})
        automation_personal_new_form = AutomationPersonalNewForm(initial={
            'human_resource': request.user.humanresource,
            'abbreviation': 'QA'
        })
        automation_personal_batch_form = AutomationPersonalBatchForm(initial={
            'abbreviation': 'QA'
        })

    personals = request.user.humanresource.automation_set.order_by('column_field')
    context = RequestContext(request, {
        'groups': groups,
        'form': automation_new_form,
        'form_personal': automation_personal_new_form,
        'form_personal_batch': automation_personal_batch_form,
        'personals': personals
    })
    return render(request, 'automations/automations.html', context)


def automation_detail(request, automation_id):
    automation = get_object_or_404(Automation, pk=automation_id)
    automation_type = request.GET.get('type', '')
    if automation_type == 'personal':
        form = AutomationPersonalForm(instance=automation)
    else:
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
    automation_type = request.GET.get('type', '')
    automation = get_object_or_404(Automation, pk=automation_id)
    if request.method == 'POST':
        if automation_type == 'personal':
            form = AutomationPersonalForm(request.POST, request.FILES, instance=automation)
        else:
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
    automation_type = request.GET.get('type', '')

    if request.method == 'POST':
        if automation_type == 'team':
            form = AutomationNewForm(request.POST, request.FILES, initial={'abbreviation': request.user.humanresource.functional_group.abbreviation})
        elif automation_type == 'personal':
            form = AutomationPersonalNewForm(request.POST, request.FILES, initial={'abbreviation': request.user.humanresource.functional_group.abbreviation,
                                                                                   'human_resource': request.user.humanresource})
        else:
            form = ''

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


def script_test(request):
    automation_id = request.GET.get('automation_id', '')
    automation = get_object_or_404(Automation, pk=automation_id)

    # execute python code read from script file of automation
    if automation.script_file:
        try:
            script_code = automation.script_file.read()
            exec(script_code)

            try:
                result = run_script(None, automation.human_resource.user.username)
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


def automation_push_personal_batch(request):
    if request.method == 'POST':
        form = AutomationPersonalBatchForm(request.POST,
                                           request.FILES,
                                           initial={
                                               'abbreviation': request.user.humanresource.functional_group.abbreviation
                                           })
        if form.is_valid():
            subteam = form.cleaned_data['subteam']
            column_field = form.cleaned_data['column_field']

            if not request.FILES:
                messages.error(request, 'No upload file selected.')
                return redirect('automations:automations')
            elif not request.FILES['script_file'].name.endswith('.py'):
                messages.error(request, 'Invalid file type, unable to upload (must be .py)')
                return redirect('automations:automations')
            elif not form.cleaned_data['script_name']:
                script_name = request.FILES['script_file'].name
            else:
                script_name = form.cleaned_data['script_name']

            for hr in subteam.humanresource_set.all():
                try:
                    automation = Automation.objects.get(human_resource=hr,
                                                        column_field=column_field)
                    automation.script_name = script_name
                    automation.script_file = request.FILES['script_file']
                    automation.save()
                except Automation.DoesNotExist:
                    Automation.objects.create(human_resource=hr,
                                              script_name=script_name,
                                              script_file=request.FILES['script_file'],
                                              column_field=column_field)
            messages.success(request, 'Script \'{0}\' pushed to subteam \'{1}\''.format(script_name, subteam))

        else:
            messages.error(request, form.errors)

        return redirect('automations:automations')
