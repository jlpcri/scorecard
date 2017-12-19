import json
from datetime import datetime

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import RequestContext
from pytz import timezone

from models import Project, ProjectPhase, Ticket
from scorecard.apps.core.views import check_user_team
from scorecard.apps.projects.forms import (ProjectNewForm, ProjectPhaseNewForm,
                                           TicketNewForm)
from scorecard.apps.users.models import FunctionalGroup, HumanResource, Subteam
from utils import REVENUE_SCALE_CHOICES


@login_required
def projects(request):
    check_user_team(request)

    function_groups = FunctionalGroup.objects.all().order_by('name')
    groups = []
    for group in function_groups:
        groups.append({
            'group': group,
            'tickets': Ticket.objects.filter(subteam__parent=group).order_by('key'),
            'projects': ProjectPhase.objects.filter(subteam__parent=group).order_by('project'),
            'subteams': [{
                'team': team,
                'tickets': Ticket.objects.filter(subteam=team).order_by('key'),
                'phases': ProjectPhase.objects.filter(subteam=team).order_by('project', 'name')
             } for team in Subteam.objects.filter(parent=group).exclude(name='Legacy')]
        })

    context = RequestContext(request, {
        'groups': groups,

        'project_new_form': ProjectNewForm(),
        'project_phase_new_form': ProjectPhaseNewForm(initial={
            'subteam': request.user.humanresource.subteam
        }),
        'ticket_new_form': TicketNewForm(initial={
            'subteam': request.user.humanresource.subteam
        }),

        'hrs': HumanResource.objects.all(),  # for ProjectPhase/Ticket edition
        'projects': Project.objects.all(),  # for ProjectPhase/Ticket edition
        'subteams': Subteam.objects.all().exclude(name='Legacy'),  # for ProjectPhase/Ticket edition
        'revenues': REVENUE_SCALE_CHOICES
    })

    return render(request, 'projects/projects.html', context)


@login_required
def project_new(request):
    if request.method == 'POST':
        form = ProjectNewForm(request.POST)
        if form.is_valid():
            project = form.save()
            messages.success(request, 'Project is added')
        else:
            messages.error(request, 'Errors found')

        return redirect('projects:projects')


@login_required
def project_edit(request):
    if request.method == 'POST':
        project_id = request.POST.get('editProjectId', '')
        project_name = request.POST.get('editProjectName', '')
        project_revenue = request.POST.get('editProjectRevenue', '')

        project = get_object_or_404(Project, pk=project_id)
        try:
            project.name = project_name
            project.revenue_scale = project_revenue
            project.save()
        except (ValidationError, IntegrityError):
            messages.error(request, 'Edit Project Name Error')

        return redirect('projects:projects')


@login_required
def project_phase_new(request):
    if request.method == 'POST':
        phase_estimate_start = request.POST.get('newPhaseEstimateStart', '')
        phase_estimate_end = request.POST.get('newPhaseEstimateEnd', '')
        phase_actual_start = request.POST.get('newPhaseActualStart', '')
        phase_actual_end = request.POST.get('newPhaseActualEnd', '')

        form = ProjectPhaseNewForm(request.POST)
        if form.is_valid():
            phase = form.save()
            if phase_estimate_start:
                phase.estimate_start = timezone(settings.TIME_ZONE).localize(datetime.strptime(phase_estimate_start, '%m/%d/%Y'))
            if phase_estimate_end:
                phase.estimate_end = timezone(settings.TIME_ZONE).localize(datetime.strptime(phase_estimate_end, '%m/%d/%Y'))
            if phase_actual_start:
                phase.actual_start = timezone(settings.TIME_ZONE).localize(datetime.strptime(phase_actual_start, '%m/%d/%Y'))
            if phase_actual_end:
                phase.actual_end = timezone(settings.TIME_ZONE).localize(datetime.strptime(phase_actual_end, '%m/%d/%Y'))
            phase.save()

            messages.success(request, 'ProjectPhase is added')
        else:
            messages.error(request, 'Errors found')

        return redirect('projects:projects')


@login_required
def project_phase_edit(request):
    if request.method == 'POST':
        phase_id = request.POST.get('editPhaseId', '')
        phase_project = request.POST.get('editPhaseProject', '')
        phase_subteam = request.POST.get('editPhaseSubteam', '')
        phase_lead = request.POST.get('editPhaseLead', '')
        phase_name = request.POST.get('editPhaseName', '')
        phase_key = request.POST.get('editPhaseKey', '')
        phase_estimate_start = request.POST.get('editPhaseEstimateStart', '')
        phase_estimate_end = request.POST.get('editPhaseEstimateEnd', '')
        phase_actual_start = request.POST.get('editPhaseActualStart', '')
        phase_actual_end = request.POST.get('editPhaseActualEnd', '')
        phase_worker = request.POST.getlist('editPhaseWorker', '')

        phase = get_object_or_404(ProjectPhase, pk=phase_id)
        try:
            phase.project = get_object_or_404(Project, pk=phase_project)
            phase.subteam = get_object_or_404(Subteam, pk=phase_subteam)
            phase.lead = get_object_or_404(HumanResource, pk=phase_lead)
            phase.name = phase_name
            phase.key = phase_key

            phase.worker.clear()
            for hr_id in phase_worker:
                phase.worker.add(hr_id)

            if phase_estimate_start:
                phase.estimate_start = timezone(settings.TIME_ZONE).localize(datetime.strptime(phase_estimate_start, '%m/%d/%Y'))
            else:
                phase.estimate_start = None
            if phase_estimate_end:
                phase.estimate_end = timezone(settings.TIME_ZONE).localize(datetime.strptime(phase_estimate_end, '%m/%d/%Y'))
            else:
                phase.estimate_end = None
            if phase_actual_start:
                phase.actual_start = timezone(settings.TIME_ZONE).localize(datetime.strptime(phase_actual_start, '%m/%d/%Y'))
            else:
                phase.actual_start = None
            if phase_actual_end:
                phase.actual_end = timezone(settings.TIME_ZONE).localize(datetime.strptime(phase_actual_end, '%m/%d/%Y'))
            else:
                phase.actual_end = None

            phase.save()
            messages.success(request, 'Project Phase is updated')
        except Exception as e:
            print e.message
            messages.error(request, 'Project Phase edit error')

        return redirect('projects:projects')


@login_required
def ticket_edit(request):
    if request.method == 'POST':
        ticket_id = request.POST.get('editTicketId', '')
        ticket_subteam = request.POST.get('editTicketSubteam', '')
        ticket_revenue = request.POST.get('editTicketRevenue', '')
        ticket_lead = request.POST.get('editTicketLead', '')
        ticket_key = request.POST.get('editTicketKey', '')
        ticket_estimate_start = request.POST.get('editTicketEstimateStart', '')
        ticket_estimate_end = request.POST.get('editTicketEstimateEnd', '')
        ticket_actual_start = request.POST.get('editTicketActualStart', '')
        ticket_actual_end = request.POST.get('editTicketActualEnd', '')
        ticket_worker = request.POST.getlist('editTicketWorker', '')

        ticket = get_object_or_404(Ticket, pk=ticket_id)
        try:
            ticket.key = ticket_key
            ticket.subteam = get_object_or_404(Subteam, pk=ticket_subteam)
            ticket.revenue_scale = ticket_revenue
            ticket.lead = get_object_or_404(HumanResource, pk=ticket_lead)
            ticket.worker.clear()
            for hr_id in ticket_worker:
                ticket.worker.add(hr_id)

            if ticket_estimate_start:
                ticket.estimate_start = timezone(settings.TIME_ZONE).localize(datetime.strptime(ticket_estimate_start, '%m/%d/%Y'))
            else:
                ticket.estimate_start = None
            if ticket_estimate_end:
                ticket.estimate_end = timezone(settings.TIME_ZONE).localize(datetime.strptime(ticket_estimate_end, '%m/%d/%Y'))
            else:
                ticket.estimate_end = None
            if ticket_actual_start:
                ticket.actual_start = timezone(settings.TIME_ZONE).localize(datetime.strptime(ticket_actual_start, '%m/%d/%Y'))
            else:
                ticket.actual_start = None
            if ticket_actual_end:
                ticket.actual_end = timezone(settings.TIME_ZONE).localize(datetime.strptime(ticket_actual_end, '%m/%d/%Y'))
            else:
                ticket.actual_end = None

            ticket.save()
            messages.success(request, 'Ticket is updated')
        except (ValidationError, IntegrityError):
            messages.error(request, 'Edit Ticket Error')

        return redirect('projects:projects')


@login_required
def ticket_new(request):
    if request.method == 'POST':
        ticket_estimate_start = request.POST.get('newTicketEstimateStart', '')
        ticket_estimate_end = request.POST.get('newTicketEstimateEnd', '')
        ticket_actual_start = request.POST.get('newTicketActualStart', '')
        ticket_actual_end = request.POST.get('newTicketActualEnd', '')
        form = TicketNewForm(request.POST)

        if form.is_valid():
            ticket = form.save()
            if ticket_estimate_start:
                ticket.estimate_start = timezone(settings.TIME_ZONE).localize(datetime.strptime(ticket_estimate_start, '%m/%d/%Y'))
            if ticket_estimate_end:
                ticket.estimate_end = timezone(settings.TIME_ZONE).localize(datetime.strptime(ticket_estimate_end, '%m/%d/%Y'))
            if ticket_actual_start:
                ticket.actual_start = timezone(settings.TIME_ZONE).localize(datetime.strptime(ticket_actual_start, '%m/%d/%Y'))
            if ticket_actual_end:
                ticket.actual_end = timezone(settings.TIME_ZONE).localize(datetime.strptime(ticket_actual_end, '%m/%d/%Y'))
            ticket.save()

            messages.success(request, 'Ticket is added')
        else:
            messages.error(request, 'Errors found')

        return redirect('projects:projects')


def fetch_workers(request):
    data = []
    id = request.GET.get('id', '')
    type = request.GET.get('type', '')
    if type == 'phase':
        item = ProjectPhase.objects.get(pk=id)
    elif type == 'ticket':
        item = Ticket.objects.get(pk=id)

    for hr in item.worker.all():
        data.append(hr.id)

    return HttpResponse(json.dumps(data), content_type='application/json')
