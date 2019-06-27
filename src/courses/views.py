from django.shortcuts import render, redirect, Http404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TestForm
from django.views.generic.edit import FormView
from django.forms import formset_factory
from .models import Statistics, Chapter

from .models import Questionnaire, Question, QuestionAnswer
# Create your views here.


class CoursePageView(LoginRequiredMixin, TemplateView):

    template_name = ['courses/course.html']
    breadcrumbs = ['course']

    def get(self, request, *args, **kwargs):
        user = request.user

        chapters = Chapter.objects.all()
        context = {
            'chapters': chapters
        }

        return render(request, self.template_name, context)


class CourseChapterRedirectView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        user = request.user

        return redirect(f'/course/chapter/{user.profile.test_taking}/')


class CourseChapterPageView(LoginRequiredMixin, TemplateView):
    template_name = 'courses/chapter.html'
    breadcrumbs = ['course']

    def get(self, request, chapter_id, *args, **kwargs):
        user = request.user

        try:
            chapter = Chapter.objects.get(id=chapter_id)
        except:
            raise Http404('Chapter does not exist')

        context = {
            'chapter': chapter
        }

        return render(request, self.template_name, context)


class CourseTestRedirectView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        user = request.user
        return redirect(f'/course/Questionnaire/{user.profile.test_taking}/')


class CourseTestPageView(LoginRequiredMixin, TemplateView):
    template_name = 'courses/Questionnaire.html'
    breadcrumbs = ['course']

    bad_at = {
        1: 'Syntax',
        2: 'File Management',
        3: 'Databases'
    }

    def get(self, request, id, *args, **kwargs):
        user = request.user
        limit = Question.objects.filter(questionnaire__name=f'Chapter {id}', show=True).count()
        if id is None:
            id = user.profile.chapter_studying

        if id > user.profile.chapter_studying:
            return redirect(f'/course/Questionnaire/{user.profile.test_taking}/')

        try:
            form = TestForm(chapter=f'Chapter {id}', limit=limit)
        except:
            raise Http404('Questionnaire does not exist')

        context = {
            'form': form,
            'id': id
        }

        return render(request, self.template_name, context)

    def post(self, request, id, *args, **kwargs):
        user = request.user
        limit = Question.objects.filter(questionnaire__name=f'Chapter {id}', show=True).count()
        form = TestForm(request.POST, chapter=f'Chapter {id}', limit=limit)

        if form.is_valid():

            quest = Questionnaire.objects.get(name=f'Chapter {id}')

            stats, created = Statistics.objects.get_or_create(user=user, questionnaire=quest)
            data = form.cleaned_data

            # Adjust user profile
            stats.answers_correct += data['correct_answers']
            stats.answers_wrong += limit - data['correct_answers']
            stats.times_taken += 1
            stats.answers_total += limit

            if stats.answers_wrong > 0:
                stats.success_rate = round(stats.answers_correct / stats.answers_wrong, 2) * 100

                if self.bad_at[id] not in user.profile.bad_at:
                    if stats.success_rate < 60.0:
                        user.profile.bad_at += f' {self.bad_at[id]}'

                else:
                    if stats.success_rate > 60.0:
                        user.profile.bad_at = user.profile.bad_at.replace(f' {self.bad_at[id]}', '')

            if data['correct_answers'] >= int(limit / 2):
                stats.passed = True
                if user.profile.chapter_studying == id:
                    user.profile.chapter_studying += 1
                    user.profile.test_taking += 1

            user.save()
            stats.save()

            try:
                next_chapter = Chapter.objects.get(id=id+1)
            except:
                return redirect('/course/completed/')

            return redirect(f'/course/chapter/{id+1}/')


        form = TestForm(chapter=f'Chapter {id}', limit=limit)

        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class CourseCompletedPageView(LoginRequiredMixin, TemplateView):

    template_name = 'courses/completed.html'
    breadcrumbs = ['course']


    def get(self, request, *args, **kwargs):
        user = request.user

        context = {

        }

        return render(request, self.template_name, context)

