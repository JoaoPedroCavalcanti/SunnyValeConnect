from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadyOnlyForAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if request.method in SAFE_METHODS:
            return True
        return False