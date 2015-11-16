from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def exportations(request):
    return render(request, 'exportations/exportations.html')

