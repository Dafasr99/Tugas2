from django.forms import ModelForm
from study_tracker import Assignment

class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['name', 'type', 'subject', 'date', 'progress', 'description']