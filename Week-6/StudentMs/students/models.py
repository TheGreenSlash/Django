from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.IntegerField()
    student_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    program = models.CharField(max_length=200)
    section = models.CharField(max_length= 5)
    enrollment_year = models.DateField()
    active_status = models.BooleanField(default=True)


