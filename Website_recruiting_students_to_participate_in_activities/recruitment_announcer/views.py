from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render

from recruitment_announcer.models import db_create_activity

# Create your views here.
from recruitment_announcer.forms import forms_create_activity
# Create your views here.

def create_activity(req):
    form = forms_create_activity()
    if req.method == 'POST':
        form = forms_create_activity(req.POST,req.FILES)
        if form.is_valid():
            form.save()
    return render(req, 'recruitment_announcer/create_activity.html',{
        'form':form,
        'db': db_create_activity.objects.all()
        })

def home(req):
    c = db_create_activity.objects.all()
    return render(req, 
           'recruitment_announcer/home.html',
           {'db': c,})

def delete(req, id):
    k = db_create_activity.objects.get(pk=id)
    k.delete()
    return redirect('create_activity')
    