from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def individuals(request):
    return render(request, 'individuals/individuals.html')