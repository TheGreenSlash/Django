from rest_framework.response import Response
from rest_framework import generics, views
from . import serializers
from . import models 

class CreateGradeView(generics.ListCreateAPIView):
    queryset = models.Grade.objects.all()
    serializer_class = serializers.GradeSerializer

class StudentGradeView(generics.ListAPIView):
    serializer_class = serializers.GradeSerializer

    def get_queryset(self):
        student = self.kwargs['pk']
        return models.Grade.objects.filter(student =student)
 

class CreateAssesmentView(generics.ListCreateAPIView):
    queryset = models.Assesment.objects.all()
    serializer_class = serializers.AssesmentSerializer
   
class SubjectsListCreateView(generics.ListCreateAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer

class GetAssesmentView(generics.ListAPIView):
    serializer_class = serializers.AssesmentSerializer

    def get_queryset(self):
        assesment = self.kwargs['pk']
        return models.Assesment.objects.filter(id=assesment)
 
