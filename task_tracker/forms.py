from django import forms
from .models import Task

class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date']
        widgets = {
            'due_date': DateInput()
        }

class LoginForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()