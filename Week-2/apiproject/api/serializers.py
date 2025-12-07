from rest_framework import serializers
from .models import Student, User, Teacher, Course, Enrollment, Attendance, Mark


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class CoursesSerializer(serializers.ModelSerializer):
    teacher = TeachersSerializer(read_only=True)
    class Meta:
        model = Course
        fields = '__all__'



class StudentSerializer(serializers.ModelSerializer):
    courses = CoursesSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class EnrollmentStudentSerializer(EnrollmentSerializer):
    student = StudentSerializer()

class EnrollmentCourseSerializer(EnrollmentSerializer):
    course = CoursesSerializer()



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]



class MarkAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class AttendanceSerializer(MarkAttendanceSerializer):
    student = StudentSerializer()
    


class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'