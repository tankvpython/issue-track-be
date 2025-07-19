from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created_by = models.ForeignKey(User, related_name='tags_created', on_delete=models.CASCADE, null=True)
    updated_by = models.ForeignKey(User, related_name='tags_updated', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Priority(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    created_by = models.ForeignKey(User, related_name='priorities_created', on_delete=models.CASCADE, null=True)
    updated_by = models.ForeignKey(User, related_name='priorities_updated', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Issue(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('CLOSED', 'Closed'),
    ]
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name='issues')
    created_by = models.ForeignKey(User, related_name='issues_created', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='issues_updated', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='issues_assigned', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class IssueLog(models.Model):
    ACTION_CHOICES = [
        ('CREATED', 'Created'),
        ('UPDATED', 'Updated'),
        ('STATUS_CHANGED', 'Status Changed'),
        ('COMMENTED', 'Commented'),
        ('DELETED', 'Deleted'),
    ]

    issue = models.ForeignKey(Issue, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    performed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(User, related_name='issuelogs_created', on_delete=models.CASCADE, null=True)
    updated_by = models.ForeignKey(User, related_name='issuelogs_updated', on_delete=models.CASCADE, null=True)

class Invitation(models.Model):
    board = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    token = models.CharField(max_length=100)
    invited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    invited_at = models.DateTimeField(auto_now_add=True)
    accepted_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='invitations_created', on_delete=models.CASCADE, null=True)
    updated_by = models.ForeignKey(User, related_name='invitations_updated', on_delete=models.CASCADE, null=True)