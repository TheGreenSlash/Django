from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import status , generics

# Create your views here.
class ListCreateCourseView(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerialzer

class ListCreateEnrollmentView(generics.ListCreateAPIView):
    queryset = models.Enrollment.objects.all()
    serializer_class = serializers.EnrollmentSerializer