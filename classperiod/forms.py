from django import forms
from .models import ClassPeriod

class ClassPeriodForm(forms.ModelForm):
    class Meta:
        model = ClassPeriod
        fields = "__all__"