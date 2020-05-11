from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model , logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse , HttpResponseRedirect , JsonResponse
from django.urls import reverse , reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin


from django.views.generic import FormView, TemplateView, RedirectView

# Create your views here.

class LoginView(SuccessMessageMixin, auth_views.LoginView):
    """Login view."""
    template_name = 'users/login.html'
    success_message = "Empieza a comprar lo que quieras a donde lo quieras!"

    # def form_valid(self, form):
    #     """Security check complete. Log the user in."""
    #     self.request.session["cart"] = []
    #     print(self.request.session["cart"])
    #     return HttpResponseRedirect(reverse("index"))

# class LoginView(FormView):
#     form_class = AuthenticationForm
#     template_name = "users/login.html"
#     success_url =  reverse_lazy("index")
#
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated == True:
#             request.session["cart"] = []
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return super(LoginView, self).dispatch(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         login(self.request, form.get_user())
#         self.request.session["cart"] = []
#         print(self.request.session.key)
#         return super(LoginView, self).form_valid(form)

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    template_name = 'users/logged_out.html'
