from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Institution, Course, Student, Enrollment, Analytics
from .serializers import InstitutionSerializer, CourseSerializer, StudentSerializer, EnrollmentSerializer, AnalyticsSerializer
from .permissions import IsAdmin, IsAdminOrReadOnly, IsAdminOrInstructor, IsStudentOrAdminOrReadOnly


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = [IsAdminOrReadOnly]  # Only admins can delete or modify, others can view.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]  # Only admins can delete or modify, others can view.
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrInstructor]  # Only admins and instructors can manage students.

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAdmin]  # Only admins can view and modify analytics.

class AnalyticsViewSet(viewsets.ModelViewSet):
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer
    permission_classes = [IsAdmin]  # Only admins can view and modify analytics.
