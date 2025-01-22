from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import AnonymousUser


class RoleValidationMiddleware(MiddlewareMixin):
    """
    Middleware to validate user roles globally.
    """
    def process_request(self, request):
        if request.user.is_authenticated:
            # Check if the user has a valid role
            if not hasattr(request.user, 'userprofile') or not request.user.userprofile.role:
                return JsonResponse({'error': 'Invalid role assigned to user'}, status=403)
        return None
    
class JWTAuthenticationMiddleware(MiddlewareMixin):
    """
    Middleware to authenticate users via JWT in non-DRF views.
    """
    def process_request(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            try:
                access_token = AccessToken(token)
                request.user = access_token.user
            except Exception:
                request.user = AnonymousUser()
        return None
    
