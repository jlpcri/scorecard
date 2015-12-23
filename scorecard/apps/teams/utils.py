from scorecard.apps.users.models import FunctionalGroup


def context_teams():
    functional_groups = FunctionalGroup.objects.all()
    for functional_group in functional_groups:
        if functional_group.key == 'PQ':
            pqs = functional_group.testmetrics_set.all().order_by('created')
        elif functional_group.key == 'QA':
            qas = functional_group.testmetrics_set.all().order_by('created')
        elif functional_group.key == 'QI':
            qis = functional_group.innovationmetrics_set.all().order_by('created')
        elif functional_group.key == 'RE':
            res = functional_group.requirementmetrics_set.all().order_by('created')
        elif functional_group.key == 'TE':
            tes = functional_group.testmetrics_set.all().order_by('created')
        elif functional_group.key == 'TL':
            tls = functional_group.labmetrics_set.all().order_by('created')

    context = {
        'pqs': pqs,
        'qas': qas,
        'qis': qis,
        'res': res,
        'tes': tes,
        'tls': tls,
    }

    return context
