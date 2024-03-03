from django.urls import path, include
from register_login.views import login, register,logout
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login,name='login'),
    path('register/',register,name='register'),
    path('logout/',logout,name='logout'),
]
