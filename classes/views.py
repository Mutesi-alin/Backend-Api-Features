
from django.shortcuts import render
from .forms import ClassesForm

def register_classes(request):
    form = ClassesForm()
    return render(request, "classes/register_classes.html", {"form": form})
