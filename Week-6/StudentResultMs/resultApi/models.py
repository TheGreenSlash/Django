from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Subject(models.Model):
    subject_code = models.CharField(unique=True)
    subject_name = models.CharField(max_length=200, unique=True)
    full_marks = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.subject_name

class Assesment(models.Model):
    assesment_types = {'FT': "First Terminal", 'ST': "Second Terminal", 'CBT' : "Class Based Test", 'Final' : "Final Term"}
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assesment_type = models.CharField(max_length=10, choices=assesment_types)
    max_marks = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"({self.assesment_type})+{self.subject.__str__()}"

class Grade(models.Model):
    student = models.IntegerField()
    assesment = models.ForeignKey(Assesment, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    
    def __str__(self):
        return f"({self.student})_{self.assesment.__str__()}"

