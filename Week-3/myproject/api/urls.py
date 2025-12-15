from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.ListCreateCourseView.as_view(), name='Courses Available'),
    path('enrollment/', views.ListCreateEnrollmentView.as_view(), name='Enrollments')
]