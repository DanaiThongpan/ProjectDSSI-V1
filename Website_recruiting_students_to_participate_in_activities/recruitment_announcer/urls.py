from django.urls import path
from recruitment_announcer.views import *

urlpatterns = [
    path('',home, name='home1'),
    path('create_activity/', create_activity, name='create_activity'),
    path('delete/<int:id>/', delete, name='delete'),
    path('activity/<int:id>/', activityre),
    path('update_activity/<int:id>/', update_activity, name="update_activity"),
]
