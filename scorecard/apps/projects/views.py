from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext

from models import Project, ProjectPhase, Ticket
from scorecard.apps.projects.forms import ProjectForm, TicketNewForm
from scorecard.apps.projects.utils import get_projects_tickets_from_fg
from scorecard.apps.users.models import FunctionalGroup


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

        'project_form_new': ProjectForm(),
        'ticket_form_new': TicketNewForm()
    })

    return render(request, 'projects/projects.html', context)


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
def project_new(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            messages.success(request, 'Project is added')
        else:
            messages.error(request, 'Errors found')

        return redirect('projects:projects')


@login_required
def ticket_detail(request, ticket_id):
    pass


@login_required
def ticket_edit(request, ticket_id):
    pass


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
