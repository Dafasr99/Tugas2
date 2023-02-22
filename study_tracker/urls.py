from django.urls import path
from . import views

app_name = 'study_tracker'

urlpatterns = [
    path('', views.assignment_list, name='assignment_list'),
]
