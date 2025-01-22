from rest_framework import serializers
from .models import Institution, Course, Student, Enrollment, Analytics

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer()

    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    course = CourseSerializer()

    class Meta:
        model = Enrollment
        fields = '__all__'

class AnalyticsSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Analytics
        fields = '__all__'
