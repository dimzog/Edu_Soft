from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TestForm

from .models import Questionnaire, Question, QuestionAnswer, UserAnswer
# Create your views here.


class CoursePageView(LoginRequiredMixin, TemplateView):

    template_name = 'courses/course.html'
    breadcrumbs = ['course']


class CourseChapter1PageView(LoginRequiredMixin, TemplateView):
    template_name = 'courses/chapter_1.html'
    breadcrumbs = ['course']


class CourseChapter2PageView(LoginRequiredMixin, TemplateView):
    template_name = 'courses/chapter_2.html'
    breadcrumbs = ['course']

    def get(self, request, *args, **kwargs):
        user = request.user

        if user.profile.chapter_studying < 2:

            return redirect('course')

        return render(request, self.template_name, {})


class CourseChapter3PageView(LoginRequiredMixin, TemplateView):
    template_name = 'courses/chapter_3.html'
    breadcrumbs = ['course']

    def get(self, request, *args, **kwargs):
        user = request.user

        if user.profile.chapter_studying < 3:
            return redirect('course')

        return render(request, self.template_name, {})


class CourseTestPageView(LoginRequiredMixin, TemplateView):
    template_name = 'courses/Questionnaire.html'
    breadcrumbs = ['course']
    form = None

    def get(self, request, *args, **kwargs):
        user = request.user
        self.form = TestForm()

        # Adjust test shown based on user progress
        TestForm.chapter = f'Chapter {user.profile.test_taking}'
        TestForm.limit = 5

        context = {
            'form': self.form
        }

        return render(request, self.template_name, context)



