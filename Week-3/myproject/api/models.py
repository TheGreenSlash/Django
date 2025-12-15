from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(User):
    pass


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.course_name
    
class Enrollment(models.Model):
    student_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name
