from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home" ),
    path('students/', views.students, name="students" ),
    path('students/<int:pk>/', views.student_detail, name="student-detail" ),
    path('students/attendace/', views.student_attendance, name="students-attendance"),
    path('students/attendace/create', views.create_attendance, name="create-attendance"),
    path('students/<int:pk>/attendance/', views.student_attendance_summary, name="student-attendance-summary" ),
    path('students/create', views.create_student, name="create-student" ),
    path('students/grade', views.grade_students, name="grade-students" ),
    path('students/<int:pk>/report/', views.student_reportcard, name="student-reportcard" ),

    path('teachers/', views.teachers, name="teachers" ),


    path('subjects/', views.subjects, name="subjects" ),
    path('subjects/enrollments/', views.enrollments, name="enrollments" ),
    path('subjects/enrollments/enroll', views.enroll_student, name="enroll" ),
    path('subjects/assesments/', views.view_assesments, name="assesments" ),
    path('subjects/assesments/create', views.create_assessment, name="create-assesment" ),
]