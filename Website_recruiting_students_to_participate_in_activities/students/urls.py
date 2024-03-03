from django.urls import path
from students.views import *

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',login_required(home,login_url="/login"), name='home'),
]
