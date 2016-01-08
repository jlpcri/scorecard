from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import RequestContext

from scorecard.apps.users.models import FunctionalGroup


@login_required
def projects(request):
    function_groups = FunctionalGroup.objects.all()
    for function_group in function_groups:
        if function_group.key == 'PQ':
            pass
        elif function_group.key == 'QA':
            qa_projects = []
            qa_tickets = function_group.ticket_set.all()
            qa_phases = function_group.projectphase_set.all()
            for phase in qa_phases:
                if phase.project in qa_projects:
                    continue
                qa_projects.append(phase.project)

    context = RequestContext(request, {
        'qa_projects': qa_projects,
        'qa_tickets': qa_tickets
    })

    return render(request, 'projects/projects.html', context)
