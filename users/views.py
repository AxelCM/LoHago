from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model , logout, login
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    template_name = 'users/logged_out.html'
