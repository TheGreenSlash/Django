from django.urls import path
from . import views


urlpatterns = [
    path('grade/', views.CreateGradeView.as_view()),
    path('grade/<int:pk>/', views.StudentGradeView.as_view()),
    path('assesment/', views.CreateAssesmentView.as_view()),
    path('assesment/<int:pk>/', views.GetAssesmentView.as_view()),
    path('subject/', views.SubjectsListCreateView.as_view()),
]