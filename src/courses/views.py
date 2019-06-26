from django.shortcuts import render, redirect, Http404
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
    limit = 3

    def get(self, request, *args, **kwargs):
        user = request.user

        form = TestForm(limit=self.limit, chapter='Chapter 1')

        # Adjust test rendered based on user progress
        # form.chapter = f'Chapter {user.profile.test_taking}'

        context = {
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user = request.user

        form = TestForm(request.POST, limit=self.limit, chapter='Chapter 1')

        if form.is_valid():

            data = form.cleaned_data
            print(data['correct_answers'])

            # Adjust user profile
            user.profile.test_1_correct += data['correct_answers']
            user.profile.test_1_wrong += self.limit - data['correct_answers']
            user.profile.test_1_times += 1
            user.profile.test_1_total += self.limit
            user.profile.test_1_success_rate = round(user.profile.test_1_correct / user.profile.test_1_wrong, 2)

            user.profile.save()

            # form = TestForm(limit=self.limit)

        context = {
            'form': form
        }

        return render(request, self.template_name, context)



