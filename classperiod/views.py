from django.shortcuts import render
from .forms import ClassPeriodForm

def register_classperiod(request):
    form = ClassPeriodForm()
    return render(request, "classperiod/register_classperiod.html", {"form": form})