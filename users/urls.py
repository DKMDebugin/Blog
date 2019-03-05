'''
    Users app urls module
'''
from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
        # login page
        path(r'login/', LoginView.as_view(template_name='users/login.html'), name='login'),
        # Logout page
        path(r'logout/', views.logout_view, name='logout'),
        # Register page
        path(r'register/', views.register, name='register'),
]
