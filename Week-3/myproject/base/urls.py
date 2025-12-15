from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_page, name='courses'),
    path('enroll/', views.enrollment_page, name='enroll')
]