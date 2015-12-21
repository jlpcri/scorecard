from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext

from models import TestMetrics, RequirementMetrics, InnovationMetrics, LabMetrics, TestMetricsConfiguration
from forms import InnovationForm, LabForm, RequirementForm, TestForm
from scorecard.apps.users.views import user_is_superuser, user_is_manager
from tasks import weekly_metric_new, weekly_send_email
from utils import context_teams


@login_required
def teams(request):
    context = RequestContext(request, context_teams())

    return render(request, 'teams/teams.html', context)


@login_required
@user_passes_test(user_is_superuser)
def weekly_metric_new_manually(request):
    """
    Manually add new metric
    :param request:
    :return:
    """

    result = weekly_metric_new()
    if not result['valid']:
        messages.error(request, result['message'])

    return HttpResponseRedirect(reverse('teams:teams'))


@login_required
@user_passes_test(user_is_superuser)
def send_email(request):
    weekly_send_email()

    return HttpResponseRedirect(reverse('teams:teams'))


@login_required
@user_passes_test(user_is_manager)
def metric_detail(request, metric_id):
    key = request.GET.get('key', '')
    try:
        test_metric_config = TestMetricsConfiguration.objects.get(functional_group__key=key)
    except TestMetricsConfiguration.DoesNotExist:
        test_metric_config = ''

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
        'test_metric_config': test_metric_config
    })

    return render(request, 'teams/metric_detail.html', context)


@login_required
@user_passes_test(user_is_manager)
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
            metric = form.save()
            if not metric.updated:
                metric.updated = True
                metric.save()

            context = context_teams()
            context['key'] = key
            return render(request, 'teams/teams.html', context)
        else:
            messages.error(request, 'Correct errors in the form')
            context = RequestContext(request, {
                'metric': metric,
                'form': form
            })
            return render(request, 'teams/metric_detail.html', context)
    else:
        return redirect('teams:teams')
