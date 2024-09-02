from django.shortcuts import  redirect
from django .shortcuts import render
from .forms import StudentRegistrationForm

def register_student(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)  
        if form.is_valid():  
            form.save() 
            return redirect("register_student") 

    else:
        form = StudentRegistrationForm() 

    return render(request, "student/register_student.html", {"form": form})  


     