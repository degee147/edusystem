from rest_framework import serializers
from .models import Institution, Course, Student, Enrollment, Analytics

class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
    course_count = serializers.SerializerMethodField()

    class Meta:
        model = Institution
        fields = '__all__'

    def get_course_count(self, obj):
        return Course.objects.filter(institution=obj).count()


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    institution = InstitutionSerializer(read_only=True)  # Display full Institution data

    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    institution = InstitutionSerializer()
    class Meta:
        model = Student
        fields = '__all__'
class EnrollmentSerializer(serializers.HyperlinkedModelSerializer):
    student = StudentSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = '__all__'

class AnalyticsSerializer(serializers.HyperlinkedModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Analytics
        fields = '__all__'
