from rest_framework import serializers
from . import models

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Enrollment
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attendance
        fields = '__all__'

class AssesmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Assesment
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Grade
        fields = '__all__'

    def validate(self, attrs):
        marks = attrs.get(
        "marks_obtained",
        getattr(self.instance, "marks_obtained", None)
        )

    
        assesment = attrs.get(
            "assesment",
            getattr(self.instance, "assesment", None)
        )
        
        student = attrs.get(
            "student",
            getattr(self.instance, "student", None)
        )
        
        grade_object = models.Grade.objects.filter(student=student, assesment=assesment)

        if grade_object.count() > 0:
            raise serializers.ValidationError(
                {'Assesment':'Assesment has already been graded'}
            )

        if marks is None or assesment is None:
            return attrs

        if marks < 0:
            raise serializers.ValidationError(
                {'marks_obtained':'Marks cannot be less that 0'}
            )
        if marks > assesment.max_marks:
            raise serializers.ValidationError({
                'marks_obtained': (f'Marks cannot be grater than ({assesment.max_marks})')
            })
        
        return attrs