from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

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


class CourseTest1PageView(LoginRequiredMixin, TemplateView):
    template_name = 'courses/test_1.html'
    breadcrumbs = ['course']

    def get(self, request, *args, **kwargs):
        user = request.user

        quest = Questionnaire.objects.select_related().get(version='Chapter 1')
        qs = quest.questions.order_by('?').all()[:2]

        for q in qs:
            print(f'Question: {q}')
            for a in q.question_answer.all():

                if a.is_valid:
                    print(f'This answer is the correct one! {a}')
                else:
                    print(f'Anser: {a}')

            print('')

        return render(request, self.template_name, {})



