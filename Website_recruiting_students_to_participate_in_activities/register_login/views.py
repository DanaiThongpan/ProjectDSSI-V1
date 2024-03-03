from django.shortcuts import render, redirect
from django.contrib.auth import (
            authenticate, 
            login as auth_login, 
            logout as auth_logout
        )
from students.models import register_studens

# Create your views here.
from .forms import forms_register_studens
# Create your views here.

def register(req):
    form = forms_register_studens()
    if req.method == 'POST':
        form = forms_register_studens(req.POST)
        if form.is_valid():
            form.save()
        return redirect('login')

    return render(req, 'register_login/register.html',{
        'form':form,
        'db': register_studens.objects.all()
        })

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        u = authenticate(request, username=username, password=password)
        if u is not None:
            # print("you're loggged iinnnn.")
            auth_login(request, u)
            if request.user.is_staff:
                return redirect('home1')
            else:
                return redirect('/students')
    return render(request, 'register_login/login.html')


def logout(request):
    auth_logout(request)
    return redirect('login')