from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Institution, Course, Student, Enrollment, Analytics
from .serializers import (
    InstitutionSerializer,
    CourseSerializer,
    StudentSerializer,
    EnrollmentSerializer,
    AnalyticsSerializer
)
from .permissions import IsAdmin, IsAdminOrReadOnly, IsAdminOrInstructor


class InstitutionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing institutions.

    **Allowed Methods**:
    - GET: List all institutions or retrieve a specific one.
    - POST: Create a new institution (Admin only).
    - PUT/PATCH: Update an institution (Admin only).
    - DELETE: Delete an institution (Admin only).

    **Permissions**:
    - Admins: Full access.
    - Others: Read-only access.

    **Example Payload** (POST/PUT):
    ```
    {
        "name": "Institution Name",
        "address": "123 Main Street",
        "domain": "institution.com",
        "config": {
            "setting1": "value1",
            "setting2": "value2"
        }
    }
    ```
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing courses.

    **Allowed Methods**:
    - GET: List all courses or retrieve a specific one.
    - POST: Create a new course (Admin only).
    - PUT/PATCH: Update a course (Admin only).
    - DELETE: Delete a course (Admin only).

    **Permissions**:
    - Admins: Full access.
    - Others: Read-only access.

    **Example Payload** (POST/PUT):
    ```
    {
        "institution": 1,
        "name": "Course Name",
        "description": "Course description",
        "max_students": 100
    }
    ```
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing students.

    **Allowed Methods**:
    - GET: List all students or retrieve a specific one.
    - POST: Create a new student (Admin/Instructor only).
    - PUT/PATCH: Update a student (Admin/Instructor only).
    - DELETE: Delete a student (Admin/Instructor only).

    **Permissions**:
    - Admins and Instructors: Full access.
    - Others: No access.

    **Example Payload** (POST/PUT):
    ```
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "institution": 1
    }
    ```
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrInstructor]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing enrollments.

    **Allowed Methods**:
    - GET: List all enrollments or retrieve a specific one.
    - POST: Enroll a student in a course (Admin only).
    - PUT/PATCH: Update an enrollment (Admin only).
    - DELETE: Delete an enrollment (Admin only).

    **Permissions**:
    - Admins: Full access.
    - Others: No access.

    **Example Payload** (POST/PUT):
    ```
    {
        "student": 1,
        "course": 1,
        "status": "enrolled",
        "active": true
    }
    ```
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class AnalyticsViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing analytics.

    **Allowed Methods**:
    - GET: Retrieve analytics data for a course.
    - POST: Create analytics data for a course (Admin only).
    - PUT/PATCH: Update analytics data (Admin only).
    - DELETE: Delete analytics data (Admin only).

    **Permissions**:
    - Admins: Full access.
    - Others: No access.

    **Example Payload** (POST/PUT):
    ```
    {
        "course": 1,
        "total_enrollments": 50,
        "completed_courses": 30,
        "average_grade": 85.5,
        "completion_rate": 75.0,
        "active_students": 20
    }
    ```
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer
