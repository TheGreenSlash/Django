from django.urls import path
from .views import LoginApi, StudentView, StudentDetailView, StudentCourseView, StudentAttendanceView,StudentAttendanceSummary,StudentGradesView,StudentReportView, UserView, TeacherView, TeacherDetailView, CoursesView, CourseDetailView, CourseStudentsView, CourseEnrollStudentView, CourseAttendanceView, CourseAttendanceMarkView, CourseGradeView

urlpatterns = [
    path('students/', StudentView.as_view(), name="students"),
    path('students/<int:pk>/', StudentDetailView.as_view(), name="student-detail"),
    path('students/<int:pk>/courses/', StudentCourseView.as_view(), name="student-courses"),
    path('students/<int:pk>/attendance/', StudentAttendanceView.as_view(), name="student-attendance"),
    path('students/<int:pk>/grades/', StudentGradesView.as_view(), name="student-grades"),
    path('students/<int:pk>/grades/', StudentGradesView.as_view(), name="student-grades"),
    path('students/<int:pk>/attendance/summary', StudentAttendanceSummary.as_view(), name="student-attendance-summary"),
    path('users/', UserView.as_view(), name="users"),
    path('login/', LoginApi.as_view(), name="login"),

    path('teachers/', TeacherView.as_view(), name="teachers"),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name="teacher-detail"),

    path('courses/', CoursesView.as_view(), name="courses"),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name="course-detail"),
    path('courses/<int:pk>/enroll/', CourseEnrollStudentView.as_view(), name="enroll-student"),
    path('courses/<int:pk>/students/', CourseStudentsView.as_view(), name="course-students"),
    path('courses/<int:pk>/attendance/', CourseAttendanceView.as_view(), name="course-attendance"),
    path('courses/<int:pk>/attendance/mark/', CourseAttendanceMarkView.as_view(), name="mark-course-attendance"),
    path('courses/<int:pk>/grade/', CourseGradeView.as_view(), name="grade-course"),
]