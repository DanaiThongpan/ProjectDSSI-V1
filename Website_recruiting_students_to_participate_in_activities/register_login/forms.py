from django import forms
from students.models import register_studens
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class forms_register_studens(UserCreationForm):


    class Meta:
        model = User
        fields = ["username","first_name","email","password1","password2"]
    
        labels = {
            'username' : 'ชื่อผู้ใช้งาน',
            'first_name' : 'ชื่อ'
        }