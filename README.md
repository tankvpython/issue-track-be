# Mini Issue Tracker

## Overview
This project is a mini issue tracker built using Django and Django REST Framework (DRF). It provides a backend solution for managing issues, tags, priorities, issue logs, and team invitations, similar to platforms like Jira.

## Features
- JWT-based authentication for secure access.
- CRUD APIs for managing issues, tags, priorities, and issue logs.
- Invitation system for team collaboration.
- Custom permissions to control access to resources.

## Models
The application includes the following models:
- **Issue**: Represents an issue with fields for title, description, status, priority, tags, and user information.
- **Tag**: Represents tags that can be associated with issues.
- **Priority**: Represents the priority level of an issue.
- **IssueLog**: Tracks changes made to issues.
- **Invitation**: Manages team invitations to join boards.

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd mini_issue_track_be
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```
  superuser cred
  username: admin
  email: admin@yopmail.com
  Pass: Admin@123

  test user cred
  username: demo
  pass: Admin@123

6. Run the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints
- **Authentication**:
  - POST `/api/auth/register/` - Register a new user.
  - POST `/api/auth/login/` - Log in a user.
  - POST `/api/auth/token/refresh/` - Refresh JWT token.

- **Issues**:
  - GET `/api/issues/issues/` - List all issues.
  - POST `/api/issues/issues/` - Create a new issue.
  - GET `/api/issues/issues/{id}/` - Retrieve a specific issue.
  - PUT/PATCH `/api/issues/issues/{id}/` - Update a specific issue.
  - DELETE `/api/issues/issues/{id}/` - Delete a specific issue.

- **Tags**:
  - GET `/api/tags/` - List all tags.
  - POST `/api/tags/` - Create a new tag.

- **Priorities**:
  - GET `/api/priorities/` - List all priorities.
  - POST `/api/priorities/` - Create a new priority.

- **Issue Logs**:
  - GET `/api/issue-logs/` - List all issue logs.
  - POST `/api/issue-logs/` - Create a new issue log.

- **Invitations**:
  - GET `/api/invitations/` - List all invitations.
  - POST `/api/invitations/` - Create a new invitation.

## Testing
To run the tests, use the following command:
```
python manage.py test
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.