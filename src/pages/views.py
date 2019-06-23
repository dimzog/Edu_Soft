from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

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


class CodePageView(LoginRequiredMixin, TemplateView):
    template_name = 'code.html'
    breadcrumbs = ['code']

