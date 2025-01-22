from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.userprofile.role == 'admin'


class IsAdminOrReadOnly(BasePermission):
    """
    Admins can perform all actions. Others can only read.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # Allow safe methods (GET, HEAD, OPTIONS)
        return request.user.is_authenticated and request.user.userprofile.role == 'admin'


class IsAdminOrInstructor(BasePermission):
    """
    Allows access to admins and instructors.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.userprofile.role in ['admin', 'instructor']


class IsStudentOrAdminOrReadOnly(BasePermission):
    """
    Students and admins can perform actions, others can only read.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.userprofile.role in ['admin', 'student']
