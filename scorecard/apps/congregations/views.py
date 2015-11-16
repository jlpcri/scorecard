from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def congregations(request):
    return render(request, 'congregations/congregations.html')

