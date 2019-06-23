from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class CodePageView(LoginRequiredMixin, TemplateView):
    template_name = 'courses/code.html'
    breadcrumbs = ['code']
