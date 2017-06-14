from django.forms import ModelForm
from django import forms
from .models import Report


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['user', 'device', 'location',
        'date', 'time']