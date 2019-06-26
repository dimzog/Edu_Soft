from django.shortcuts import render, redirect, Http404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TestForm
from django.views.generic.edit import FormView
from django.forms import formset_factory
from .models import Statistics

from .models import Questionnaire, Question, QuestionAnswer
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



class CourseTestRedirectView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        user = request.user
        return redirect(f'/course/Questionnaire/{user.profile.test_taking}/')


class CourseTestPageView(LoginRequiredMixin, TemplateView):
    template_name = 'courses/Questionnaire.html'
    breadcrumbs = ['course']
    limit = 0

    def get(self, request, id, *args, **kwargs):
        user = request.user

        if id is None:
            id = user.profile.chapter_studying

        if id > user.profile.chapter_studying:
            return redirect(f'/course/Questionnaire/{user.profile.test_taking}/')

        try:
            form = TestForm(chapter=f'Chapter {id}', limit=self.limit)
        except:
            raise Http404('Questionnaire does not exist')

        context = {
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, id, *args, **kwargs):
        user = request.user
        form = TestForm(request.POST, chapter=f'Chapter {id}', limit=self.limit)

        if form.is_valid():

            quest = Questionnaire.objects.filter(name=f'Chapter {id}').first()
            stats, created = Statistics.objects.get_or_create(user=user, questionnaire=quest)
            data = form.cleaned_data

            # Adjust user profile
            stats.answers_correct += data['correct_answers']
            stats.answers_wrong += self.limit - data['correct_answers']
            stats.times_taken += 1
            stats.answers_total += self.limit

            if stats.answers_wrong > 0:
                stats.success_rate = round(stats.answers_correct / stats.answers_wrong, 2)

            #if data['correct_answers'] > (self.limit / 2) + 1:
            #    if user.profile.chapter_studying == 1:
            #        user.profile.chapter_studying += 1
            #        user.profile.test_taking += 1
            #        user.profile.level = 'Intermediate'

            #else:
            #    user.profile.bad_at('Syntax')

            stats.save()



        context = {
            'form': form
        }

        return render(request, self.template_name, context)



