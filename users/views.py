from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model , logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse , HttpResponseRedirect , JsonResponse
from django.urls import reverse , reverse_lazy


# Create your views here.

class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'users/login.html'

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        self.request.session["cart"] = []
        return HttpResponseRedirect(reverse("index"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    template_name = 'users/logged_out.html'
