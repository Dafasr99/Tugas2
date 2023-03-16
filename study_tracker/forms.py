from django import forms
from django.forms import ModelForm, NumberInput
from study_tracker.models import Assignment

class AssignmentForm(ModelForm):
 
    class Meta:
        model = Assignment
        fields = ['name', 'type', 'subject', 'progress', 'description']
        
