from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from .models import register_studens
from recruitment_announcer.models import db_create_activity

# from .forms import forms_register_studens
# Create your views here.

# def register(req):
#     form = forms_register_studens()
#     if req.method == 'POST':
#         form = forms_register_studens(req.POST)
#         if form.is_valid():
#             form.save()
#     return render(req, 'register.html',{
#         'form':form,
#         'db': register_studens.objects.all()
#         })
# @login_required

def home(req):
    c = db_create_activity.objects.all()
    return render(req, 'students/home.html',{'db':c})