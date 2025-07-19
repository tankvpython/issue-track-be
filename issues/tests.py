from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Issue, Tag, Priority, IssueLog, Invitation
from django.contrib.auth import get_user_model

User = get_user_model()

class IssueTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.issue = Issue.objects.create(
            title='Test Issue',
            description='This is a test issue.',
            status='OPEN',
            created_by=self.user,
            assigned_to=self.user
        )

    def test_create_issue(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('issue-list'), {
            'title': 'New Issue',
            'description': 'Description of new issue.',
            'status': 'OPEN',
            'created_by': self.user.id,
            'assigned_to': self.user.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_issues(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('issue-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_issue(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.patch(reverse('issue-detail', args=[self.issue.id]), {
            'title': 'Updated Issue Title'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.issue.refresh_from_db()
        self.assertEqual(self.issue.title, 'Updated Issue Title')

    def test_delete_issue(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(reverse('issue-detail', args=[self.issue.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Issue.objects.filter(id=self.issue.id).exists())

class TagTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.tag = Tag.objects.create(name='Bug', slug='bug')

    def test_create_tag(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('tag-list'), {
            'name': 'Feature',
            'slug': 'feature'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_tags(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('tag-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class PriorityTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.priority = Priority.objects.create(name='High', level=1)

    def test_create_priority(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('priority-list'), {
            'name': 'Medium',
            'level': 2
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_priorities(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('priority-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class InvitationTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.invitation = Invitation.objects.create(
            email='invitee@example.com',
            invited_by=self.user,
            accepted=False
        )

    def test_create_invitation(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('invitation-list'), {
            'email': 'newinvitee@example.com',
            'invited_by': self.user.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_invitations(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('invitation-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)