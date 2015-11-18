from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext

from models import  TestMetrics, RequirementMetrics, InnovationMetrics, LabMetrics
from forms import InnovationForm


@login_required
def teams(request):
    qis = InnovationMetrics.objects.all()
    tls = LabMetrics.objects.all()
    res = RequirementMetrics.objects.all()
    pqs = TestMetrics.objects.filter(functional_group__key='PQ')
    qas = TestMetrics.objects.filter(functional_group__key='QA')
    tes = TestMetrics.objects.filter(functional_group__key='TE')

    qi_form = InnovationForm()

    context = RequestContext(request, {
        'pqs': pqs,
        'qas': qas,
        'qis': qis,
        'res': res,
        'tes': tes,
        'tls': tls,

        'qi_form': qi_form
    })
    return render(request, 'teams/teams.html', context)


def qi_new(request):
    if request.method == 'POST':
        form = InnovationForm(request.POST)
        if form.is_valid():
            qi = form.save()
            messages.success(request, 'Quality Innovation Metric is added')
            return redirect('teams:teams')
        else:
            messages.error(request, 'Correct errors in the form')
            context = RequestContext(request, {
                'form': form,
                'operation': settings.METRIC_OPERATION['new']
            })
            return render(request, 'teams/quality_innovation_detail.html', context)
    else:
        form = InnovationForm()
        context = RequestContext(request, {
            'form': form,
            'operation': settings.METRIC_OPERATION['new']
        })
        return render(request, 'teams/quality_innovation_detail.html', context)


def qi_detail(request, qi_id):
    qi = get_object_or_404(InnovationMetrics, pk=qi_id)
    form = InnovationForm(instance=qi)
    context = RequestContext(request, {
        'qi': qi,
        'form': form,
        'operation': settings.METRIC_OPERATION['detail']
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
