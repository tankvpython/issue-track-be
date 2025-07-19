from rest_framework import serializers
from .models import Issue, Tag, Priority, IssueLog, Invitation

class IssueSerializer(serializers.ModelSerializer):
    assigned_name = serializers.SerializerMethodField()
    priority_name = serializers.SerializerMethodField()
    tags_names = serializers.SerializerMethodField()
    
    # Make fields optional
    priority = serializers.PrimaryKeyRelatedField(required=False, allow_null=True, queryset=Issue._meta.get_field('priority').related_model.objects.all())
    assigned_to = serializers.PrimaryKeyRelatedField(required=False, allow_null=True, queryset=Issue._meta.get_field('assigned_to').related_model.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, required=False, queryset=Issue._meta.get_field('tags').related_model.objects.all())
    
    class Meta:
        model = Issue
        exclude = ('created_by', 'updated_by')
        
    # Get assigned user's username
    def get_assigned_name(self, obj):
        return obj.assigned_to.username if obj.assigned_to else None

    # Get priority name
    def get_priority_name(self, obj):
        return obj.priority.name if obj.priority else None

    # Get list of tag names
    def get_tags_names(self, obj):
        return [tag.name for tag in obj.tags.all()]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ('created_by', 'updated_by')

class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        exclude = ('created_by', 'updated_by')

class IssueLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueLog
        exclude = ('created_by', 'updated_by')

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        exclude = ('created_by', 'updated_by')