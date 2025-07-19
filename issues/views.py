from rest_framework import viewsets
from rest_framework.response import Response
from .models import Issue, Tag, Priority, IssueLog, Invitation
from django.db.models import Q
from .serializers import IssueSerializer, TagSerializer, PrioritySerializer, IssueLogSerializer, InvitationSerializer
from issues.permissions import IsIssueCreator, IsInvitedUser
from rest_framework import permissions as drf_permissions
from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import PermissionDenied


class IssueViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [drf_permissions.IsAuthenticated, IsIssueCreator]
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
    
    def get_queryset(self):
        print("issue viewset called")
        user = self.request.user
        if user.is_authenticated:
            return self.queryset.filter(Q(created_by=user) | Q(assigned_to=user))

        return self.queryset.none()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response({"detail": "Issue list data not found"}, status=200)
        return super().list(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.created_by != request.user:
            raise PermissionDenied("You can only delete issues you created.")
        self.perform_destroy(instance)
        return Response({"detail": "Issue deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class TagViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [drf_permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response({"detail": "Tag list data not found"}, status=200)
        return super().list(request, *args, **kwargs)

class PriorityViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = [drf_permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response({"detail": "Priority list data not found"}, status=200)
        return super().list(request, *args, **kwargs)

class IssueLogViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
    queryset = IssueLog.objects.all()
    serializer_class = IssueLogSerializer
    permission_classes = [drf_permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response({"detail": "IssueLog list data not found"}, status=200)
        return super().list(request, *args, **kwargs)

class InvitationViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    permission_classes = [drf_permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response({"detail": "Invitation list data not found"}, status=200)
        return super().list(request, *args, **kwargs)
    
    
# html rendering view
def welcome(request):
    return render(request, "welcome.html")
