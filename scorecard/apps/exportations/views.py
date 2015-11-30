from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook

from scorecard.apps.users.models import FunctionalGroup
from scorecard.apps.teams.models import InnovationMetrics


@login_required
def exportations(request):
    functional_groups = FunctionalGroup.objects.all().order_by('name')
    data = {}
    data_name = []
    data_key = []
    for functional_group in functional_groups:
        data_name.append(functional_group.name)
        data_key.append(functional_group.key)

    dates = InnovationMetrics.objects.values_list('created', flat=True)
    data['name'] = data_name
    data['key'] = data_key
    data['dates'] = dates

    context = RequestContext(request, {
        'data': data
    })

    return render(request, 'exportations/exportations.html', context)


@login_required
def export_excel(request):
    functional_groups = FunctionalGroup.objects.all().order_by('name')
    key = request.GET.get('key', '')
    date = request.GET.get('date', '')
    # print key, date

    wb = Workbook()
    wb.active.title = 'Testing Summary'

    if key == 'SU':
        for functional_group in functional_groups:
            ws = wb.create_sheet(functional_group.name)
    else:
        ws = wb.create_sheet(key)

    response = HttpResponse(save_virtual_workbook(wb), content_type='application/vnd.ms-excel')
    response['Content-disposition'] = 'attachment; filename="foo.xlsx"'
    return response
