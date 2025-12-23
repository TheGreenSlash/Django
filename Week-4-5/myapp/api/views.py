from rest_framework.response import Response
from rest_framework import generics, views
from . import serializers
from . import models 


class StudentsListView(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentDetailView(generics.ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        return models.Student.objects.filter(id=id)
    
class StudentEnrollmentsView(generics.ListAPIView):
    serializer_class = serializers.EnrollmentSerializer

    def get_queryset(self):
        student_id = self.kwargs['pk']
        return models.Enrollment.objects.filter(student_id =student_id)

class StudentAttendanceView(generics.ListAPIView):
    serializer_class = serializers.AttendanceSerializer

    def get_queryset(self):
        student_id = self.kwargs['pk']
        return models.Attendance.objects.filter(student_id =student_id)
    
class StudentAttendanceSummary(views.APIView):
    def get(self, request, pk):
        attendance = models.Attendance.objects.filter(student_id=self.kwargs['pk'])
        total_days = attendance.count()
        present_days = 0
        student_name = []
        for entry in attendance:
            student_name = entry.student.__str__()
            if entry.status == "P":
                present_days += 1
        print(present_days)

        absent_days = total_days - present_days
        attendance_percentage = round((present_days/total_days)*100, 2)
        data = {
            "Student" : student_name,
            "Total Classes" : total_days,
            "Present" : present_days,
            "Absent" : absent_days,
            "Attendance(%)" : attendance_percentage

        }
        return Response(data)

class CreateGradeView(generics.ListCreateAPIView):
    queryset = models.Grade.objects.all()
    serializer_class = serializers.GradeSerializer

class StudentGradeView(generics.ListAPIView):
    serializer_class = serializers.GradeSerializer

    def get_queryset(self):
        student_id = self.kwargs['pk']
        return models.Grade.objects.filter(student_id =student_id)
 

class StudentReportSummary(views.APIView):
    def get(self, request, pk):
        grades = models.Grade.objects.filter(student_id=self.kwargs['pk'])
        total_subjects = grades.count()
        total_marks = 0
        scored_marks = 0
        student_name = []
        for entry in grades:
            student_name = entry.student.__str__()
            scored_marks += entry.marks_obtained
            total_marks += entry.assesment.max_marks
        result = ""
        if (scored_marks > total_marks/2):
            result = "Pass"
        else:
            result = "NG"
        
        result_percentage = 0
        if scored_marks != 0:
            result_percentage = round((scored_marks/total_marks)*100, 2)

        data ={}
        if student_name:
            data = {
                "Student" : student_name,
                "Subjects Graded" : total_subjects,
                "Full Marks" : total_marks,
                "Marks Obtained" : scored_marks,
                "Result" : result,
                "Percentage" : result_percentage

            }
        else:
            data = {
                "Error" : "This Student Does Not Exist"
            }
        return Response(data)


class CreateAttendanceView(generics.ListCreateAPIView):
    queryset = models.Attendance.objects.all()
    serializer_class = serializers.AttendanceSerializer


class TeachersListView(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer

class TeacherSubjectView(generics.ListAPIView):
    serializer_class = serializers.SubjectSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['pk']
        return models.Subject.objects.filter(teacher_id = teacher_id)
 

class SubjectsListView(generics.ListCreateAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer

class SubjectStudentsView(generics.ListAPIView):
    serializer_class = serializers.EnrollmentSerializer

    def get_queryset(self):
        subject_id = self.kwargs['pk']
        return models.Enrollment.objects.filter(subject_id=subject_id)

class SubjectAttendanceView(generics.ListAPIView):
    serializer_class = serializers.AttendanceSerializer

    def get_queryset(self):
        subject_id = self.kwargs['pk']
        return models.Attendance.objects.filter(subject_id=subject_id)
  


class CreateEnrollmentView(generics.ListCreateAPIView):
    queryset = models.Enrollment.objects.all()
    serializer_class = serializers.EnrollmentSerializer


class CreateAssesmentView(generics.ListCreateAPIView):
    queryset = models.Assesment.objects.all()
    serializer_class = serializers.AssesmentSerializer
    

class SubjectAssesmentView(generics.ListAPIView):
    serializer_class = serializers.AssesmentSerializer

    def get_queryset(self):
        subject_id = self.kwargs['pk']
        return models.Assesment.objects.filter(subject_id =subject_id)
