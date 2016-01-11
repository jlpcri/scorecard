from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext

from models import Project, ProjectPhase, Ticket
from scorecard.apps.projects.forms import ProjectNewForm, TicketNewForm, ProjectPhaseNewForm
from scorecard.apps.projects.utils import get_projects_tickets_from_fg
from scorecard.apps.users.models import FunctionalGroup, HumanResource


@login_required
def projects(request):
    function_groups = FunctionalGroup.objects.all()

    pqs = qas = tes = qis = res = tls = {}

    for function_group in function_groups:
        if function_group.key == 'PQ':
            pqs = get_projects_tickets_from_fg(function_group)
        elif function_group.key == 'QA':
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
        'pq_projects': pqs['fg_projects'],
        'pq_tickets': pqs['fg_tickets'],
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
        'leads': HumanResource.objects.all()
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
    pass


@login_required
def ticket_edit(request):
    if request.method == 'POST':
        ticket_id = request.POST.get('editTicketId', '')
        ticket_fg = request.POST.get('editTicketFunctionalGroup', '')
        ticket_lead = request.POST.get('editTicketLead', '')
        ticket_key = request.POST.get('editTicketKey', '')

        ticket = get_object_or_404(Ticket, pk=ticket_id)
        try:
            ticket.key = ticket_key
            ticket.functional_group = get_object_or_404(FunctionalGroup, pk=ticket_fg)
            ticket.lead = get_object_or_404(HumanResource, pk=ticket_lead)
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
