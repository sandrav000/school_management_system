from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import User, Student, LibraryHistory, FeesHistory
from .serializers import UserSerializer, StudentSerializer, LibraryHistorySerializer, FeesHistorySerializer
from .permissions import IsAdmin, IsOfficeStaff, IsLibrarian


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing User accounts.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]


class StudentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Student records.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdmin()]
        return [permissions.IsAuthenticated()]


class LibraryHistoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Library History.
    """
    queryset = LibraryHistory.objects.all()
    serializer_class = LibraryHistorySerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            if self.request.user.role != 'admin':
                raise PermissionDenied("Only admin can modify library history.")
        elif self.action in ['list', 'retrieve']:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated()]


class FeesHistoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Fees History.
    """
    queryset = FeesHistory.objects.all()
    serializer_class = FeesHistorySerializer

    def get_permissions(self):
        if self.request.user.role in ['admin', 'staff']:
            return [permissions.IsAuthenticated()]
        else:
            raise PermissionDenied("You do not have permission to manage fees history.")
