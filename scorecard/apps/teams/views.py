from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def teams(request):
    return render(request, 'teams/teams.html')

