from datetime import date
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
    today = date.today()
    if today.isoweekday() == 5:
        try:
            qi = InnovationMetrics.objects.latest('created')
            if qi.created.date() == today:
                messages.error(request, 'Metric is already exist')
            else:
                weekly_metric_new()
        except InnovationMetrics.DoesNotExist:
            weekly_metric_new()
    else:
        messages.error(request, 'Today is not Friday')
    return HttpResponseRedirect(reverse('teams:teams'))


def metric_detail(request, metric_id):
    key = request.GET.get('key', '')

    if key in ['PQ', 'QA', 'TE']:
        metric = get_object_or_404(TestMetrics, pk=metric_id)
        form = TestForm(instance=metric)
    elif key == 'QI':
        metric = get_object_or_404(InnovationMetrics, pk=metric_id)
        form = InnovationForm(instance=metric)
    elif key == 'RE':
        metric = get_object_or_404(RequirementMetrics, pk=metric_id)
        form = RequirementForm(instance=metric)
    elif key == 'TL':
        metric = get_object_or_404(LabMetrics, pk=metric_id)
        form = LabForm(instance=metric)
    else:
        messages.error(request, 'No key to Functional Group found')
        return redirect('teams:teams')

    # qi = get_object_or_404(InnovationMetrics, pk=qi_id)
    # form = InnovationForm(instance=qi)
    context = RequestContext(request, {
        'metric': metric,
        'form': form,
    })

    return render(request, 'teams/metric_detail.html', context)


def metric_edit(request, metric_id):
    key = request.GET.get('key', '')

    if request.method == 'POST':
        if key in ['PQ', 'QA', 'TE']:
            metric = get_object_or_404(TestMetrics, pk=metric_id)
            form = TestForm(request.POST, instance=metric)
        elif key == 'QI':
            metric = get_object_or_404(InnovationMetrics, pk=metric_id)
            form = InnovationForm(request.POST, instance=metric)
        elif key == 'RE':
            metric = get_object_or_404(RequirementMetrics, pk=metric_id)
            form = RequirementForm(request.POST, instance=metric)
        elif key == 'TL':
            metric = get_object_or_404(LabMetrics, pk=metric_id)
            form = LabForm(request.POST, instance=metric)
        else:
            messages.error(request, 'No key to Functional Group found')
            return redirect('teams:teams')

        if form.is_valid():
            form.save()
            return redirect('teams:teams')
        else:
            messages.error(request, 'Correct errors in the form')
            context = RequestContext(request, {
                'form': form
            })
            return render(request, 'teams/metric_detail.html', context)
    else:
        return redirect('teams:teams')
