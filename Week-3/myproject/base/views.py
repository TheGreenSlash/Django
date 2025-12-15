from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse

# Create your views here.
def course_page(request):
    try:
        courses = requests.get("http://127.0.0.1:8000/api/course").json()
    except:
        return HttpResponse("Errorssss")
    
    return render(request , 'base/courses.html', {'courses': courses})

def enrollment_page(request):
    if request.method == 'POST':
        data = {
            "student_name" : request.POST.get("student_name"),
            "email" : request.POST.get("email"),
            "course" : request.POST.get("course"),

        }
        response = requests.post("http://127.0.0.1:8000/api/enrollment", json=data)

        if response.status_code == 201:
            return redirect('success')
        
    try:
        courses = requests.get("http://127.0.0.1:8000/api/course").json()
    except:
        return HttpResponse("Errorssss")
    
    return render(request , 'base/enrollment.html', {'courses': courses})