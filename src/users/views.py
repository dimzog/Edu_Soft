from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class RegisterPageView(TemplateView):
    template_name = 'users/register.html'
    breadcrumbs = ['register']


class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
    breadcrumbs = ['profile']
