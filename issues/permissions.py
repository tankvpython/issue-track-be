from rest_framework import permissions
from rest_framework.permissions import BasePermission

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authenticated users to edit issues.
    Unauthenticated users can only view issues.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

class IsIssueCreator(permissions.BasePermission):
    """
    Custom permission to only allow the creator of an issue to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user

class IsInvitedUser(permissions.BasePermission):
    """
    Custom permission to only allow invited users to access the issue board.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_invited

class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
