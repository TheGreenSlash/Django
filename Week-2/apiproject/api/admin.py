from django.contrib import admin
from .models import Student, Teacher, Course, Enrollment, Mark, Attendance, User
# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Mark)
admin.site.register(Attendance)
