from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, StudentViewSet, LibraryHistoryViewSet, FeesHistoryViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('students', StudentViewSet)
router.register('library-history', LibraryHistoryViewSet)
router.register('fees-history', FeesHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]






