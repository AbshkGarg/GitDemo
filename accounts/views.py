from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# The SignupView redirects to login because we set
# success_url = reverse_lazy('login') . The Login page redirects to the homepage
# because in our blog_project/settings.py file we set LOGIN_REDIRECT_URL = 'home' .
