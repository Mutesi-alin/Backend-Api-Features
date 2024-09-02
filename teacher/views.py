from django.shortcuts import render
from .forms import teacherForm

def register_teacher(request):
    form = teacherForm()
    return render(request, "teacher/register_teacher.html", {"form": form})