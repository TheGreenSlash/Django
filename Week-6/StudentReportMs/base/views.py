from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import services

# Create your views here.
def home(request):
    return render(request , 'base/home.html')


def students(request):
    students = services.getStudentsAll()
    return render(request, 'base/students.html', {"students" : students })

def student_detail(request, pk):
    student = services.getStudent(pk)

    if student is None:
        return HttpResponse("Error 404: Not Found")
    else:
        return render(request, 'base/student-detail.html', {"student":student[0]})


def create_student(request):

    status = services.createStudent(request)
    if status is not None:
        if status.status_code == 201:
            return redirect('subjects')
        
        else:
            return HttpResponse("Something went wrong")
        
    
    
    return render(request, 'base/create-student.html')

def create_subject(request):

    status = services.createSubject(request)
    
    if status is not None:
        if status.status_code == 201:
            return redirect('subjects')
        
        else:
            return HttpResponse("Something went wrong")
        
    return render(request, 'base/create-subject.html')


def subjects(request):
    subjects = services.getSubjectsAll()
    return render(request, 'base/subjects.html', {"subjects" : subjects })

def assesments(request):
    assesments = services.getAssesmentsAll()
    return render(request, 'base/assesments.html', {"assesments" : assesments })

def create_assesment(request):

    status = services.createAssesment(request)
    subjects = services.getSubjectsAll()
    if status is not None:
        if status.status_code == 201 or 200:
            return redirect('assesments')
        else:
            return HttpResponse("Something went wrong")
        
    return render(request, 'base/create-assesments.html', {"subjects":subjects})

def create_grade(request):

    status = services.createGrades(request)
    students = services.getStudentsAll()
    assesments = services.getAssesmentsAll()
    if status is not None:
        if status.status_code == 201 or 200:
            return redirect('home')
        else:
            return HttpResponse("Something went wrong")
        
    return render(request, 'base/create-grades.html', {"students":students, "assesments":assesments})

def report(request, pk):
    data = services.getReport(pk)

    if data is None:
        return HttpResponse("Something went wrong")
    else:
        return render(request , 'base/report.html', {"report":data})
    
    
