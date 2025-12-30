from django.urls import path
from . import views


urlpatterns = [
    path('students/', views.StudentCreateApiView.as_view()),
    path('students/<int:pk>/', views.StudentDetailView.as_view()),
]