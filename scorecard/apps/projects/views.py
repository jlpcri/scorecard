from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from pytz import timezone

from models import Project, ProjectPhase, Ticket
from scorecard.apps.projects.forms import ProjectNewForm, TicketNewForm, ProjectPhaseNewForm
from scorecard.apps.projects.utils import get_projects_tickets_from_fg
from scorecard.apps.users.models import FunctionalGroup, HumanResource


@login_required
def projects(request):
    function_groups = FunctionalGroup.objects.all()

    qas = tes = qis = res = tls = {
        'fg_projects': [],
        'fg_tickets': []
    }

    for function_group in function_groups:
        if function_group.key == 'QA':
            qas = get_projects_tickets_from_fg(function_group)
        elif function_group.key == 'TE':
            tes = get_projects_tickets_from_fg(function_group)
        elif function_group.key == 'QI':
            qis = get_projects_tickets_from_fg(function_group)
        elif function_group.key == 'RE':
            res = get_projects_tickets_from_fg(function_group)
        elif function_group.key == 'TL':
            tls = get_projects_tickets_from_fg(function_group)

    context = RequestContext(request, {
        'qa_projects': qas['fg_projects'],
        'qa_tickets': qas['fg_tickets'],
        'te_projects': tes['fg_projects'],
        'te_tickets': tes['fg_tickets'],
        'qi_projects': qis['fg_projects'],
        'qi_tickets': qis['fg_tickets'],
        're_projects': res['fg_projects'],
        're_tickets': res['fg_tickets'],
        'tl_projects': tls['fg_projects'],
        'tl_tickets': tls['fg_tickets'],

        'project_new_form': ProjectNewForm(),
        'project_phase_new_form': ProjectPhaseNewForm(),
        'ticket_new_form': TicketNewForm(),

        'function_groups': function_groups,
        'leads': HumanResource.objects.all(),
        'projects': Project.objects.all()
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

        project = get_object_or_404(Project, pk=project_id)
        try:
            project.name = project_name
            project.save()
        except (ValidationError, IntegrityError):
            messages.error(request, 'Edit Project Name Error')

        return redirect('projects:projects')


@login_required
def project_phase_new(request):
    if request.method == 'POST':
        form = ProjectPhaseNewForm(request.POST)
        if form.is_valid():
            phase = form.save()
            messages.success(request, 'ProjecPhase is added')
        else:
            messages.error(request, 'Errors found')

        return redirect('projects:projects')


@login_required
def project_phase_edit(request):
    if request.method == 'POST':
        phase_id = request.POST.get('editPhaseId', '')
        phase_project = request.POST.get('editPhaseProject', '')
        phase_fg = request.POST.get('editPhaseFunctionalGroup', '')
        phase_lead = request.POST.get('editPhaseLead', '')
        phase_name = request.POST.get('editPhaseName', '')
        phase_key = request.POST.get('editPhaseKey', '')
        phase_estimate_start = request.POST.get('editPhaseEstimateStart', '')
        phase_estimate_end = request.POST.get('editPhaseEstimateEnd', '')
        phase_actual_start = request.POST.get('editPhaseActualStart', '')
        phase_actual_end = request.POST.get('editPhaseActualEnd', '')

        phase = get_object_or_404(ProjectPhase, pk=phase_id)
        try:
            phase.project = get_object_or_404(Project, pk=phase_project)
            phase.functional_group = get_object_or_404(FunctionalGroup, pk=phase_fg)
            phase.lead = get_object_or_404(HumanResource, pk=phase_lead)
            phase.name = phase_name
            phase.key = phase_key
            if phase_estimate_start:
                phase.estimate_start = timezone(settings.TIME_ZONE).localize(datetime.strptime(phase_estimate_start, '%m/%d/%Y'))
            if phase_estimate_end:
                phase.estimate_end = timezone(settings.TIME_ZONE).localize(datetime.strptime(phase_estimate_end, '%m/%d/%Y'))
            if phase_actual_start:
                phase.actual_start = timezone(settings.TIME_ZONE).localize(datetime.strptime(phase_actual_start, '%m/%d/%Y'))
            if phase_actual_end:
                phase.actual_end = timezone(settings.TIME_ZONE).localize(datetime.strptime(phase_actual_end, '%m/%d/%Y'))

            phase.save()
            messages.success(request, 'Project Phase is updated')
        except (ValidationError, IntegrityError):
            messages.error(request, 'Project Phase edit error')

        return redirect('projects:projects')


@login_required
def ticket_edit(request):
    if request.method == 'POST':
        ticket_id = request.POST.get('editTicketId', '')
        ticket_fg = request.POST.get('editTicketFunctionalGroup', '')
        ticket_lead = request.POST.get('editTicketLead', '')
        ticket_key = request.POST.get('editTicketKey', '')
        ticket_estimate_start = request.POST.get('editTicketEstimateStart', '')
        ticket_estimate_end = request.POST.get('editTicketEstimateEnd', '')
        ticket_actual_start = request.POST.get('editTicketActualStart', '')
        ticket_actual_end = request.POST.get('editTicketActualEnd', '')

        ticket = get_object_or_404(Ticket, pk=ticket_id)
        try:
            ticket.key = ticket_key
            ticket.functional_group = get_object_or_404(FunctionalGroup, pk=ticket_fg)
            ticket.lead = get_object_or_404(HumanResource, pk=ticket_lead)
            if ticket_estimate_start:
                ticket.estimate_start = timezone(settings.TIME_ZONE).localize(datetime.strptime(ticket_estimate_start, '%m/%d/%Y'))
            if ticket_estimate_end:
                ticket.estimate_end = timezone(settings.TIME_ZONE).localize(datetime.strptime(ticket_estimate_end, '%m/%d/%Y'))
            if ticket_actual_start:
                ticket.actual_start = timezone(settings.TIME_ZONE).localize(datetime.strptime(ticket_actual_start, '%m/%d/%Y'))
            if ticket_actual_end:
                ticket.actual_end = timezone(settings.TIME_ZONE).localize(datetime.strptime(ticket_actual_end, '%m/%d/%Y'))

            ticket.save()
            messages.success(request, 'Ticket is updated')
        except (ValidationError, IntegrityError):
            messages.error(request, 'Edit Ticket Error')

        return redirect('projects:projects')


@login_required
def ticket_new(request):
    if request.method == 'POST':
        form = TicketNewForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            messages.success(request, 'Ticket is added')
        else:
            messages.error(request, 'Errors found')

        return redirect('projects:projects')
