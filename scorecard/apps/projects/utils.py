def get_projects_tickets_from_fg(function_group):
    fg_projects = []
    fg_tickets = function_group.ticket_set.all()
    fg_phases = function_group.projectphase_set.all()
    for phase in fg_phases:
        if phase.project in fg_projects:
            continue
        fg_projects.append(phase.project)

    return {
        'fg_projects': fg_projects,
        'fg_tickets': fg_tickets
    }

