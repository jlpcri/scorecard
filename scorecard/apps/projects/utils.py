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


# Revenue Scale Options for Projects and Tickets
LARGE_REVENUE = 1
MEDIUM_REVENUE = 2
SMALL_REVENUE = 3
INTERNAL = 4
REVENUE_SCALE_CHOICES = (
    (LARGE_REVENUE, 'Greater than 1M'),
    (MEDIUM_REVENUE, 'Between 250K and 1M'),
    (SMALL_REVENUE, 'Less than 250K'),
    (INTERNAL, 'Internal')
)
