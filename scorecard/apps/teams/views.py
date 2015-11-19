from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext

from models import TestMetrics, RequirementMetrics, InnovationMetrics, LabMetrics
from forms import InnovationForm, LabForm, RequirementForm, TestForm
from scorecard.apps.users.models import FunctionalGroup
from scorecard.apps.users.views import user_is_superuser
from tasks import weekly_metric_new


@login_required
def teams(request):
    functional_groups = FunctionalGroup.objects.all()
    for functional_group in functional_groups:
        if functional_group.key == 'PQ':
            pqs = functional_group.testmetrics_set.all()
        elif functional_group.key == 'QA':
            qas = functional_group.testmetrics_set.all()
        elif functional_group.key == 'QI':
            qis = functional_group.innovationmetrics_set.all()
        elif functional_group.key == 'RE':
            res = functional_group.requirementmetrics_set.all()
        elif functional_group.key == 'TE':
            tes = functional_group.testmetrics_set.all()
        elif functional_group.key == 'TL':
            tls = functional_group.labmetrics_set.all()

    context = RequestContext(request, {
        'pqs': pqs,
        'qas': qas,
        'qis': qis,
        'res': res,
        'tes': tes,
        'tls': tls,
    })
    return render(request, 'teams/teams.html', context)


@user_passes_test(user_is_superuser)
def weekly_metric_new_manually(request):
    """
    Manually add new metric
    :param request:
    :return:
    """
    weekly_metric_new()
    return HttpResponseRedirect(reverse('teams:teams'))


def qi_detail(request, qi_id):
    qi = get_object_or_404(InnovationMetrics, pk=qi_id)
    form = InnovationForm(instance=qi)
    context = RequestContext(request, {
        'qi': qi,
        'form': form,
    })

    return render(request, 'teams/quality_innovation_detail.html', context)


def qi_edit(request, qi_id):
    qi = get_object_or_404(InnovationMetrics, pk=qi_id)
    if request.method == 'POST':
        form = InnovationForm(request.POST, instance=qi)
        if form.is_valid():
            qi = form.save()
            return redirect('teams:teams')
        else:
            messages.error(request, 'Correct errors in the form')
            context = RequestContext(request, {
                'form': form
            })
            return render(request, 'teams/quality_innovation_detail.html', context)
    else:
        return redirect('teams:teams')
