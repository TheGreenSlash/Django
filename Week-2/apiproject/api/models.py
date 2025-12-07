from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

roles = [('admin','Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student')]
class User(AbstractUser):
    username = models.CharField(unique=True, max_length=200)
    email = models.EmailField(unique=True, null=True)
    role = models.CharField(choices=roles)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    def __str__(self):
        return self.username



  
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    roll = models.IntegerField(unique=True)
    grade = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return str(self.user.username)

    


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher_profile")
    teacher_id = models.IntegerField()
    department = models.CharField(max_length=200)
    def __str__(self):
        return str(self.user.username)




class Course(models.Model):
    course_name = models.CharField()
    course_code = models.CharField()
    teacher = models.ForeignKey(Teacher , on_delete=models.CASCADE)
    description = models.TextField(max_length= 700)
    def __str__(self):
        return self.course_name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollment')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollment')
    date_enrolled = models.DateTimeField(auto_now_add=True)
    
CHOICES = (
    ('pr', 'Present'),
    ('ab', 'Absent'),
)
class Attendance(models.Model):
    student =  models.ForeignKey(Student,on_delete=models.CASCADE)  
    course =models.ForeignKey(Course,on_delete=models.CASCADE) 
    status = models.CharField(max_length=7, choices=CHOICES)
    date = models.DateField()

GPA_CHOICES = (
    ('A' ,'A'),
    ('B','B'),
    ('C','C'),
    ('D','D'),
    ('NG','NG'),
)  
class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    gpa = models.CharField(max_length=2, choices=GPA_CHOICES)
    remarks = models.TextField()