from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'
    breadcrumbs = ['home']


class AboutPageView(TemplateView):
    template_name = 'about.html'
    breadcrumbs = ['about']


class ContactPageView(TemplateView):
    template_name = 'contact.html'
    breadcrumbs = ['contact']


class CodePageView(TemplateView):
    template_name = 'code.html'
    breadcrumbs = ['code']


class LoginPageView(TemplateView):
    template_name = 'login.html'
    breadcrumbs = ['login']


class RegisterPageView(TemplateView):
    template_name = 'register.html'
    breadcrumbs = ['register']

