from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.StudentsListView.as_view()),
    path('students/<int:pk>/', views.StudentDetailView.as_view()),
    path('students/<int:pk>/enrollment/', views.StudentEnrollmentsView.as_view()),
    path('students/attendance/', views.CreateAttendanceView.as_view()),
    path('students/<int:pk>/attendance/', views.StudentAttendanceView.as_view()),
    path('students/<int:pk>/attendance/summary/', views.StudentAttendanceSummary.as_view()),
    path('students/grade/', views.CreateGradeView.as_view()),
    path('students/<int:pk>/grades/', views.StudentGradeView.as_view()),
    path('students/<int:pk>/report/', views.StudentReportSummary.as_view()),

    path('teachers/', views.TeachersListView.as_view()),
    path('teachers/<int:pk>/subjects/', views.TeacherSubjectView.as_view()),

    path('subjects/', views.SubjectsListView.as_view()),
    path('subjects/<int:pk>/students/', views.SubjectStudentsView.as_view()),
    path('subjects/<int:pk>/attendance/', views.SubjectAttendanceView.as_view()),
    path('subjects/assesment/', views.CreateAssesmentView.as_view()),
    path('subjects/<int:pk>/assesment/', views.SubjectAssesmentView.as_view()),

    path('enroll/', views.CreateEnrollmentView.as_view()),   
]