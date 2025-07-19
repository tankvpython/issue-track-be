from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Issue, IssueLog
from django.contrib.auth.models import User

@receiver(post_save, sender=Issue)
def log_issue_save(sender, instance, created, **kwargs):
    action = 'CREATED' if created else 'UPDATED'
    IssueLog.objects.create(
        issue=instance,
        action=action,
        performed_by=instance.updated_by or instance.created_by,
        notes=f'Issue {action.lower()} via API.'
    )

@receiver(post_delete, sender=Issue)
def log_issue_delete(sender, instance, **kwargs):
    IssueLog.objects.create(
        issue=instance,
        action='DELETED',
        performed_by=instance.updated_by or instance.created_by,
        notes='Issue deleted via API.'
    )
