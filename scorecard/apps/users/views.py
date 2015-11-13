from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from models import  HumanResource


@login_required
def home(request):
    return render(request, 'users/home.html')


def user_is_superuser(user):
    return user.is_superuser


def sign_in(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            if user.is_active:
                login(request, user)
                try:
                    HumanResource.objects.get(user=user)
                except HumanResource.DoesNotExist:
                    HumanResource.objects.create(user=user)
                if request.GET.get('next'):
                    return redirect(request.GET['next'])
                else:
                    return redirect('users:home')
            else:
                messages.error(request, 'This account is inactive.')
                return redirect('landing')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('landing')
    else:
        return redirect('landing')