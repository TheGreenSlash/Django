from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

# Create your views here.
def home(request):
    return render(request , 'base/home.html')

def students(request):
    students = requests.get('http://127.0.0.1:8000/api/students/').json()
    return render(request, 'base/students.html', {"students" : students })

def student_detail(request, pk):
    response = requests.get(f'http://127.0.0.1:8000/api/students/{(int)(pk)}/')
    
    if  not response:
        return HttpResponse("Page does not exist.")
    else:
        student = response.json()

        return render(request, 'base/student-detail.html', {"students" : student})

def create_attendance(request):
    if request.method == 'POST':
        data = {
            "date" : request.POST.get("date"),
            "status" : request.POST.get("status"),
            "student": request.POST.get("student"),
            "subject" : request.POST.get("subject"),
        }
        response = requests.post('http://127.0.0.1:8000/api/attendance/', json=data)
        if response.status_code == 201:
            return redirect('students-attendance')
        else:
            return HttpResponse("Something went wrong")
    students = requests.get('http://127.0.0.1:8000/api/students/').json()
    subjects = requests.get('http://127.0.0.1:8000/api/subjects/').json()
    return render(request, 'base/create-attendance.html', {"students" : students, "subjects" : subjects})


def student_attendance(request):
    attendance = requests.get('http://127.0.0.1:8000/api/students/attendance/').json()
    return render(request, 'base/attendance.html', {"attendance" : attendance})

def student_attendance_summary(request, pk):
    response = requests.get(f'http://127.0.0.1:8000/api/students/{(int)(pk)}/attendance/summary/')
    if not response:
        return HttpResponse("Page does not exist.")
    
    else:
        summary = response.json()
        context = {
        "id" : summary.get("id"),
        "student": summary.get("Student"),
        "total_classes": summary.get("Total Classes"),
        "present": summary.get("Present"),
        "absent": summary.get("Absent"),
        "attendance": summary.get("Attendance(%)"),
    }
        return render(request, 'base/student-attendance-summary.html', context)

def create_student(request):
    if request.method == 'POST':
        data = {
            "name" : request.POST.get("name"),
            "roll": request.POST.get("roll"),
            "email" : request.POST.get("email"),
            "program" : request.POST.get("program"),
            "active_status" : request.POST.get("active_status") == 'true',
        }
        response = requests.post('http://127.0.0.1:8000/api/students/', json=data)
        if response.status_code == 201:
            return redirect('base/students.html')
        else:
            return HttpResponse("Something went wrong")
        
    return render(request, 'base/create-student.html')

def enrollments(request):
    enrollments = requests.get('http://127.0.0.1:8000/api/enroll/').json()
    return render(request, 'base/enrollments.html', {"enrollments" : enrollments })

def enroll_student(request):
    if request.method == 'POST':
        data = {
            "status" : request.POST.get("status"),
            "student": request.POST.get("student"),
            "subject" : request.POST.get("subject"),
        }
        response = requests.post('http://127.0.0.1:8000/api/enroll/', json=data)
        if response.status_code == 201:
            return redirect('enrollments')
        else:
            return HttpResponse("Something went wrong")
    students = requests.get('http://127.0.0.1:8000/api/students/').json()
    subjects = requests.get('http://127.0.0.1:8000/api/subjects/').json()
    return render(request, 'base/enroll-student.html', {"students" : students, "subjects" : subjects})

def student_reportcard(request, pk):
    cardstring = f'http://127.0.0.1:8000/api/students/{pk}/report/'
    response = requests.get(cardstring).json()
    report = {
        "student" : response.get("Student"),
        "subjects_graded" : response.get("Subjects Graded"),
        "subjects_graded" : response.get("Subjects Graded"),
        "full_marks" : response.get("Full Marks"),
        "marks_obtained" : response.get("Marks Obtained"),
        "result" : response.get("Result"),
        "percentage" : response.get("Percentage"),

    }
    print(report)
    return render(request, 'base/report-card.html', {"report" : report} )
    
     
def teachers(request):
    response = requests.get('http://127.0.0.1:8000/api/teachers/')
    teachers = response.json()
    return render(request, 'base/teachers.html', {"teachers" :teachers })

def grade_students(request):
    if request.method == 'POST':
        data = {
            "marks_obtained" : request.POST.get("marks_obtained"),
            "student" : request.POST.get("student"),
            "assesment" : request.POST.get("assesment"),
            
            
        }
        response = requests.post('http://127.0.0.1:8000/api/subjects/assesment/', json=data)
        if response.status_code == 201:
            return redirect('assesments')
        else:
            return HttpResponse("Something went wrong")
    students = requests.get('http://127.0.0.1:8000/api/students/').json()
    assesments = requests.get('http://127.0.0.1:8000/api/subjects/assesment/').json()
    return render(request, 'base/grade-students.html', {"students" : students, "assesments":assesments})


def create_assessment(request):
    if request.method == 'POST':
        data = {
            "subject" : request.POST.get("subject"),
            "assesment_type" : request.POST.get("assesment_type"),
            "max_marks" : request.POST.get("max_marks"),
            "date": request.POST.get("date"),
            
        }
        response = requests.post('http://127.0.0.1:8000/api/subjects/assesment/', json=data)
        if response.status_code == 201:
            return redirect('assesments')
        else:
            return HttpResponse("Something went wrong")
    subjects = requests.get('http://127.0.0.1:8000/api/subjects/').json()
    return render(request, 'base/create-assesment.html', {"subjects" : subjects})

def view_assesments(request):
    assesments = requests.get('http://127.0.0.1:8000/api/subjects/assesment').json()
    return render(request, 'base/assesments.html', {"assesments" : assesments })

    
def subjects(request):
    subjects = requests.get('http://127.0.0.1:8000/api/subjects/').json
    return render(request, 'base/subjects.html', {"subjects":subjects} )
    