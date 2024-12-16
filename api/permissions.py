from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Grants access only to Admin users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsOfficeStaff(BasePermission):
    """
    Grants access only to Office Staff users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'staff'


class IsLibrarian(BasePermission):
    """
    Grants access only to Librarian users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'librarian'
