from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField()
    email = models.EmailField()
    program = models.CharField(max_length=200)
    active_status = models.BooleanField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Subject(models.Model):
    subject_name = models.CharField(max_length=250)
    subject_code = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)

    def __str__(self):
        return self.subject_name
    

class Enrollment(models.Model):
    statuses = {'A':"Active", 'D':"Dropped"}
       
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=statuses)
    def __str__(self):
        return f"({self.student})_enroll_{self.subject.__str__()}"


class Attendance(models.Model):
    statuses = {'A':"Absent", 'P':"Present"}
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(choices=statuses)
    def __str__(self):
        return f"({self.student})_{self.subject.__str__()}"


class Assesment(models.Model):
    assesment_types = {'FT': "First Terminal", 'ST': "Second Terminal", 'CBT' : "Class Based Test", 'Final' : "Final Term"}
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assesment_type = models.CharField(choices=assesment_types)
    max_marks = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"({self.assesment_type})+{self.subject.__str__()}"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assesment = models.ForeignKey(Assesment, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    
    def __str__(self):
        return f"({self.student})_{self.assesment.__str__()}"

