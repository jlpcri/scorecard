from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def projects(request):
    return render(request, 'projects/projects.html')
