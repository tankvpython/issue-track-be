from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IssueViewSet, TagViewSet, PriorityViewSet, IssueLogViewSet, InvitationViewSet

router = DefaultRouter()
router.register(r'issues', IssueViewSet)
router.register(r'tags', TagViewSet)
router.register(r'priorities', PriorityViewSet)
router.register(r'issue-logs', IssueLogViewSet)
router.register(r'invitations', InvitationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]