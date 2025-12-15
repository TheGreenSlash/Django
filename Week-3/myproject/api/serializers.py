from .models import User, Course, Enrollment
from rest_framework import serializers

class CourseSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'code', 'description']

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'