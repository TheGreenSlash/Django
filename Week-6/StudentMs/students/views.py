from rest_framework.response import Response
from rest_framework import generics
from . import serializers , models

# Create your views here.
class StudentCreateApiView(generics.ListCreateAPIView):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()
    
class StudentDetailView(generics.ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        return models.Student.objects.filter(id=id)
  