from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):
    work=forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    due=forms.DateField(widget= forms.DateInput(attrs={'placeholder':'Add due date...'}))
    priority=forms.IntegerField(widget= forms.TextInput(attrs={'placeholder':'Add priority ...'}))
    class Meta:
        model = Task
        fields = ['work' , 'due','donecheck','priority']
    