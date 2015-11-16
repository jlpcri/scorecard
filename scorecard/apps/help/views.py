from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def guide(request):
    return render(request, 'help/guide.html')
