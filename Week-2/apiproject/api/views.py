from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from .models import Student, Teacher, Course, User, Course,Enrollment,Attendance, Mark
from .serializers import LoginSerializer, StudentSerializer, UserSerializer,TeachersSerializer,  CoursesSerializer,EnrollmentStudentSerializer, EnrollmentCourseSerializer, EnrollmentSerializer,MarkAttendanceSerializer, AttendanceSerializer, MarksSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import DjangoModelPermissions
from django.db.models import Avg, Sum


# Create your views here.
class LoginApi(APIView):
    def post(self ,request):
        data = request.data
        serializer = LoginSerializer(data = data)
        if serializer.is_valid():
            print(serializer.data)
        
        if not serializer.is_valid():
            return Response({
                "status" : False,
                "data" : serializer.errors
            })
        username = serializer.data['username']
        password = serializer.data['password']
        user_obj = authenticate(username=username, password=password)
        print(user_obj)
        if user_obj:
            token,_ = Token.objects.get_or_create(user= user_obj)
            return Response({
                "status" : True,
                "data" : {"Token": token.key},
                "user" : serializer.data
            }) 
        return Response({
                "status" : False,
                "data" : {},
                "message" : "Invalid Credentials"
            }) 





class StudentView(generics.ListAPIView):
    # permission_classes = [DjangoModelPermissions]
    # authentication_classes = [TokenAuthentication]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [DjangoModelPermissions]
    # authentication_classes = [TokenAuthentication]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'

class StudentCourseView(generics.ListAPIView):
    # permission_classes = [DjangoModelPermissions]
    # authentication_classes = [TokenAuthentication]
    serializer_class = EnrollmentCourseSerializer

    def get_queryset(self):
        students_id = self.kwargs['pk']
        return Enrollment.objects.filter(students_id = students_id)

class StudentAttendanceView(generics.ListAPIView):
    # permission_classes = [DjangoModelPermissions]
    # authentication_classes = [TokenAuthentication]
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        student_id = self.kwargs['pk']
        return Attendance.objects.filter(student_id = student_id)

class StudentAttendanceSummary(APIView):
    def get(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"error" :  "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        subject_attendance = Attendance.objects.filter(student_id = pk)
        if not subject_attendance.exists():
            return Response({
                "student":student.user.username,
                "subjects": [],
                "overall": {
                    "Total Present": 0,
                    "Total Absent": 0,
                    "Total Entries": 0,
                    "Overall Attendance": 0,
                    
                }
            })
        
        subject_data = []
        total_present = 0
        total_absent = 0

        course_list = subject_attendance.values_list("course_id", flat=True).distinct()

        attendace = AttendanceSerializer(subject_attendance, many=True).data


        for course_id in course_list:
            course = Course.objects.get(id=course_id)

            course_records = subject_attendance.filter(course_id = course_id)
            present = course_records.filter(status="pr").count()
            absent = course_records.filter(status="ab").count()
            total = course_records.count()

            total_present += present
            total_absent += absent

            subject_data.append({
                "Couse Name": course.course_name,
                "Course Code": course.course_code,
                "Present Days": present,
                "Absent Days": absent,
                "Total Days": total,
                "Attendance(%)": round((present/total) * 100, 2) if total > 0 else 0
            })

            overall_total = total_present+total_absent
            overall_percent = round(total_present/overall_total) * 100 if overall_total > 0 else 0
       
        return Response({
            "student": student.user.username,
            "subjects": subject_data,
            "overall": {
                "total_present": total_present,
                "total_absent": total_absent,
                "total_entries": overall_total,
                "overall_attendance_percentage": round(overall_percent, 2),
            }
        })  

class StudentGradesView(generics.ListAPIView):
    # permission_classes = [DjangoModelPermissions]
    # authentication_classes = [TokenAuthentication]
    serializer_class = MarksSerializer
    def get_queryset(self):
        student_id = self.kwargs['pk']
        return Mark.objects.filter(student_id = student_id)

class StudentReportView(APIView):
    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        subject_marks = Mark.objects.filter(student_id = pk)
        marks = MarksSerializer(subject_marks, many=True).data

        stats = subject_marks.aggregate(total = Sum("score"),
                                average = Avg("score"))
        return Response({
            "student":student.user.username,
            "grade": student.grade,
            "roll": student.roll,
            "marks": subject_marks,
            "overall": {
                "total": stats["total"],
                "average": stats["average"]
            }
        })


 
    



class UserView(APIView):
    # permission_classes = [DjangoModelPermissions]
    # authentication_classes = [TokenAuthentication]
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   


class TeacherView(generics.ListCreateAPIView):
    # permission_classes = [DjangoModelPermissions]
    # authentication_classes = [TokenAuthentication]
    queryset = Teacher.objects.all()
    serializer_class= TeachersSerializer
 
class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [DjangoModelPermissions]
    # authentication_classes = [TokenAuthentication]
    queryset = Teacher.objects.all()
    serializer_class = TeachersSerializer
    lookup_field = 'pk'




class CoursesView(generics.ListAPIView):
    # permission_classes = [DjangoModelPermissions]
    # authentication_classes = [TokenAuthentication]
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    
class CourseDetailView(generics.RetrieveAPIView):
    # permission_classes = [DjangoModelPermissions]
    # authentication_classes = [TokenAuthentication]
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    lookup_field = 'pk'
    
class CourseEnrollStudentView(generics.ListCreateAPIView):
    # permission_classes = [DjangoModelPermissions]
    # authentication_classes = [TokenAuthentication]
    serializer_class = EnrollmentStudentSerializer
    def get_queryset(self):
        course_id = self.kwargs['pk']
        return Enrollment.objects.filter(course_id = course_id)

class CourseStudentsView(generics.ListAPIView):
    # permission_classes = [DjangoModelPermissions]
    # authentication_classes = [TokenAuthentication]
    serializer_class = EnrollmentStudentSerializer

    def get_queryset(self):
        course_id = self.kwargs['pk']
        return Enrollment.objects.filter(course_id = course_id)

class CourseAttendanceView(generics.ListAPIView):
    # permission_classes = [DjangoModelPermissions]
    # authentication_classes = [TokenAuthentication]
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        course_id = self.kwargs['pk']
        return Attendance.objects.filter(course_id = course_id)

class CourseAttendanceMarkView(generics.CreateAPIView):
    # permission_classes = [DjangoModelPermissions]
    # authentication_classes = [TokenAuthentication]
    serializer_class = MarkAttendanceSerializer

    def get_queryset(self):
        course_id = self.kwargs['pk']
        return Attendance.objects.filter(course_id = course_id)

class CourseGradeView(generics.CreateAPIView):
    # permission_classes = [DjangoModelPermissions]
    # authentication_classes = [TokenAuthentication]
    serializer_class = MarksSerializer

    def get_queryset(self):
        course_id = self.kwargs['pk']
        return Mark.objects.filter(course_id = course_id)


    

    

    
      