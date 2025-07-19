from django.contrib import admin
from .models import Issue, Tag, Priority, IssueLog, Invitation

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'created_by', 'assigned_to', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'priority', 'tags')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    search_fields = ('name',)

@admin.register(IssueLog)
class IssueLogAdmin(admin.ModelAdmin):
    list_display = ('issue', 'action', 'performed_by', 'timestamp', 'notes')
    list_filter = ('action', 'performed_by')

@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('email', 'invited_by', 'accepted', 'invited_at', 'accepted_at')
    search_fields = ('email',)