from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FrequentlyAskedQuestion

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


class HelpPageView(TemplateView):
    template_name = 'help.html'
    breadcrumbs = ['help']


class FaqPageView(TemplateView):
    template_name = 'faq.html'
    breadcrumbs = ['faq']


    def get(self, request, *args, **kwargs):
        user = request.user
        faqs = FrequentlyAskedQuestion.objects.all()

        context = {
            'faqs': faqs
        }

        return render(request, self.template_name, context)

