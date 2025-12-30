from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home" ),
    path('students/', views.students, name="students" ),
    path('students/<int:pk>/', views.student_detail, name="student-detail" ),
    path('students/<int:pk>/report', views.report, name="report" ),
    path('students/create', views.create_student, name="create-student" ),
    path('subjects/', views.subjects, name="subjects" ),
    path('subjects/create', views.create_subject, name="create-subject" ),
    path('assesments/', views.assesments, name="assesments" ),
    path('assesments/create', views.create_assesment, name="create-assesments" ),
    path('grade/', views.create_grade, name="grade" ),
]