from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstitutionViewSet, CourseViewSet, StudentViewSet, EnrollmentViewSet, AnalyticsViewSet

router = DefaultRouter()
router.register(r'institutions', InstitutionViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'analytics', AnalyticsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
