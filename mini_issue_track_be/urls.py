from django.contrib import admin
from django.urls import path, include
from issues.views import welcome  # Import the welcome view

urlpatterns = [
    path('', welcome, name='welcome'),  # Root route for welcome page
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/issues/', include('issues.urls')),
    # path('api/tags/', include('issues.urls')),
    # path('api/priorities/', include('issues.urls')),
    # path('api/issue-logs/', include('issues.urls')),
    # path('api/invitations/', include('issues.urls')),
]