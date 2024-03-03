from django.urls import path
from recruitment_announcer.views import home, create_activity, delete

urlpatterns = [
    path('',home, name='home1'),
    path('create_activity/', create_activity, name='create_activity'),
    path('delete/<int:id>/', delete, name='delete'),
]
