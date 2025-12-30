import requests 
from django.http import HttpResponse
from rest_framework import status
from django.shortcuts import redirect


def getStudentsAll():
    students = requests.get('http://127.0.0.1:8001/stdApi/students/').json()
    return students

def getStudent(pk:int):
    response = requests.get(f'http://127.0.0.1:8001/stdApi/students/{(int)(pk)}/')

    if  not response.json():
        return None
    else:
        return response.json()


def createStudent(request):
    if request.method == 'POST':
        data = {
            "student_name": request.POST.get("student_name"),
            "roll_no": request.POST.get("roll_no"),
            "date_of_birth": request.POST.get("date_of_birth"),
            "program": request.POST.get("program"),
            "section": request.POST.get("section"),
            "enrollment_year": request.POST.get("enrollment_year"),
            "active_status": request.POST.get("active_status") == "true",
        }

        response = requests.post(
            "http://127.0.0.1:8001/stdApi/students/",
            json=data
        )

        return response
    
def createSubject(request):
    if request.method == 'POST':
        data = {
            "subject_code": request.POST.get("subject_code"),
            "subject_name": request.POST.get("subject_name"),
            "full_marks": request.POST.get("full_marks"),
        }

        response = requests.post(
            "http://127.0.0.1:8002/resultApi/subject/",
            json=data
        )

        return response
    
def getSubjectsAll():
    subjects = requests.get('http://127.0.0.1:8002/resultApi/subject/').json()
    return subjects

def getAssesmentsAll():
    assesments = requests.get('http://127.0.0.1:8002/resultApi/assesment/').json()
    return assesments

def createAssesment(request):
    if request.method == 'POST':
        data = {
            "subject": request.POST.get("subject"),
            "assesment_type": request.POST.get("assesment_type"),
            "max_marks": request.POST.get("max_marks"),
            "date": request.POST.get("date"),
        }
        response = requests.post(
            "http://127.0.0.1:8002/resultApi/assesment/",
            json=data
        )
        return response
   
def createGrades(request):
    if request.method == 'POST':
        data = {
            "student": request.POST.get("student"),
            "assesment": request.POST.get("assesment"),
            "marks_obtained": request.POST.get("marks_obtained"),
        }
        response = requests.post(
            "http://127.0.0.1:8002/resultApi/grade/",
            json=data
        )
        return response

def getAssesment(pk:int):
    response = requests.get(f'http://127.0.0.1:8002/resultApi/assesment/{(int)(pk)}/')

    if  not response.json():
        return None
    else:
        return response.json()



def getGrade(pk:int):
    response = requests.get(f'http://127.0.0.1:8002/resultApi/grade/{(int)(pk)}/')
    print(response)
    if  not response.json():
        return None
    else:
        return response.json()

def getReport(pk:int):
        
        total_marks = 0
        scored_marks = 0
        total_subjects = 0
        result = ''
        result_percentage = 0
        grades = getGrade(pk)
        assesments = []
        student = ''
        student_name = ''
        if grades is not None:
            for grade in grades:
                total_subjects = total_subjects + 1
                assesments = (getAssesment(grade.get("assesment")))
                student = getStudent(grade.get("student"))
                scored_marks += grade.get("marks_obtained")

        if assesments is not None:
            for entry in assesments:
                total_marks += entry.get("max_marks")

            for std in student:
                student_name = std.get("student_name") 
            if student is not None:
                
                if (scored_marks > total_marks/2):
                    result = "Pass"
                else:
                    result = "NG"

                if scored_marks != 0:
                    result_percentage = round((scored_marks/total_marks)*100, 2)
            
        data ={}
        if grades is not None:
            data = {
                "student" : student_name,
                "subject_graded" : total_subjects,
                "full_marks" : total_marks,
                "marks_obtained" : scored_marks,
                "result" : result,
                "percentage" : result_percentage

            }
        else:
            data = None

        return data
