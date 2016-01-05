from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def automations(request):
    return render(request, 'automations/automations.html')

