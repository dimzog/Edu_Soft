from django.shortcuts import render, redirect, Http404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TestForm
from django.views.generic.edit import FormView
from django.forms import formset_factory
from .models import Statistics, Chapter

from .models import Questionnaire, Question, QuestionAnswer, StatisticsPerCategory, Statistics
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

        if chapter_id is None:
            chapter_id = user.profile.chapter_studying

        if chapter_id > user.profile.chapter_studying:
            return redirect(f'/course/chapter/{user.profile.chapter_studying}/')

        try:
            quest = Questionnaire.objects.get(id=chapter_id)
            stats, created = Statistics.objects.get_or_create(user=user, questionnaire=quest)
        except:
            raise Http404('Chapter should be followed by Questionnaire')

        stats.times_read += 1
        stats.save()
        context = {
            'chapter': chapter,
            'chapter_id': chapter_id
        }

        return render(request, self.template_name, context)


class CourseTestRedirectView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        user = request.user
        return redirect(f'/course/Questionnaire/{user.profile.test_taking}/')


class CourseTestPageView(LoginRequiredMixin, TemplateView):
    template_name = 'courses/Questionnaire.html'
    breadcrumbs = ['course']

    def get(self, request, id, *args, **kwargs):
        user = request.user

        if id is None:
            id = user.profile.chapter_studying

        if id > user.profile.chapter_studying:
            return redirect(f'/course/Questionnaire/{user.profile.test_taking}/')

        try:
            quest = Questionnaire.objects.get(id=id)

        except:
            return redirect('/course/completed/')

        limit = Question.objects.filter(questionnaire=quest, show=True).count()

        form = TestForm(chapter=id, limit=limit)

        context = {
            'form': form,
            'questionnaire': quest
        }

        return render(request, self.template_name, context)

    def post(self, request, id, *args, **kwargs):
        user = request.user
        quest = Questionnaire.objects.get(id=id)
        limit = Question.objects.filter(questionnaire=quest, show=True).count()
        form = TestForm(request.POST, chapter=id, limit=limit)

        if form.is_valid():

            stats, created = Statistics.objects.get_or_create(user=user, questionnaire=quest)
            data = form.cleaned_data

            # total correct answers in current questionnaire
            current_correct_answers = 0

            for i in range(limit):

                # Grab question data
                user_answer = data.get(f'question{i}')
                # for each category need to update data separate, so each loop needs to grab category statistics from DB
                stats_cat, created = StatisticsPerCategory.objects.get_or_create(user=user, category=user_answer.question.category)

                if user_answer.is_valid:
                    current_correct_answers += 1
                    stats_cat.answers_correct += 1

                else:
                    stats_cat.answers_wrong += 1

                stats_cat.answers_total += 1

                if stats_cat.answers_wrong >= stats_cat.answers_correct:
                    stats_cat.bad_at = True
#
                else:
                    stats_cat.bad_at = False

                stats_cat.save()

            stats.answers_correct += current_correct_answers
            stats.answers_wrong += limit - current_correct_answers
            stats.answers_total += limit

            stats.times_taken += 1
            stats.success_rate = round(stats.answers_correct / stats.answers_total, 2) * 100

            # if user scores 60%+, consider it success
            if current_correct_answers / limit >= 0.6:
                stats.passed = True

                if user.profile.chapter_studying == id:
                    user.profile.chapter_studying += 1
                    user.profile.test_taking += 1

                user.save()
                stats.save()

            else:
                user.save()
                stats.save()
                return redirect(f'/course/chapter/{id}/')

            # Try grabbing next chapter, if there isnt any, course is completed.

            try:
                next_chapter = Chapter.objects.get(id=id+1)

            except:

                try:
                    next_quest = Questionnaire.objects.get(id=id+1)
                except:
                    return redirect('/course/completed/')

                return redirect(f'/course/Questionnaire/{id+1}/')


            return redirect(f'/course/chapter/{id+1}/')


        context = {
            'form': form,
            'questionnaire': quest,
        }

        return render(request, self.template_name, context)


class CourseCompletedPageView(LoginRequiredMixin, TemplateView):

    template_name = 'courses/completed.html'
    breadcrumbs = ['course']

    def get(self, request, *args, **kwargs):
        user = request.user

        context = {}

        return render(request, self.template_name, context)

