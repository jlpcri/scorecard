from datetime import timedelta


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


def calculate_business_day(start, end):
    count = 0
    if end >= start:
        days = (start + timedelta(x + 1) for x in xrange((end - start).days))
    else:
        days = (end + timedelta(x + 1) for x in xrange((start - end).days))

    for day in days:
        if day.weekday() < 5:
            count += 1

    if start > end:
        count *= -1

    return count
