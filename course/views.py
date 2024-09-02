from django.shortcuts import render
from .forms import CourseForm

def register_course(request):
    form = CourseForm()
    return render(request, "course/register_course.html", {"form": form})