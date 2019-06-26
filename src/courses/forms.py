from django import forms
from .models import Questionnaire, QuestionAnswer, Question
from django.contrib.auth.models import User
from django.db import models


class TestForm(forms.Form):


    def __init__(self, *args, **kwargs):
        self.limit = kwargs.pop('limit')
        self.chapter = kwargs.pop('chapter')
        super(TestForm, self).__init__(*args, **kwargs)


        # Grab Questionnaire for current Chapter
        self.questionnaire = Questionnaire.objects.select_related().get(version=self.chapter)

        # Grab questions that are foreign keys to current Questionnaire from database, limit them.
        # self.questions = self.questionnaire.questions.order_by('?').all()[:self.limit]
        self.questions = self.questionnaire.questions.all()[:self.limit]
        print(f'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ{self.questions}')

        self.queryset = []

        for question in self.questions:

            self.queryset.append([question,
                                 QuestionAnswer.objects.filter(question=question, question__questionnaire=self.questionnaire)])

        print('\n')

        for q in self.questions:
            print(f'--- Question: {q}')
            for a in q.question_answer.all():
                print(f'Answer: {a} [x]') if a.is_valid else print(f'Answer: {a}')

        # Change select class, because of fault css
        widget = forms.Select(attrs={'class': 'browser-default'})

        # Create question for number of limit, change limit to add more
        for counter, q in enumerate(self.queryset):
            self.fields[f'question{counter}'] = forms.ModelChoiceField(label=q[0],
                                                                       queryset=q[1],
                                                                       required=True,
                                                                       to_field_name='answer',
                                                                       empty_label=None,
                                                                       widget=widget
                                                                       )

    def clean(self):

        print(f'>>>>>>>>>>>>>>>>>>>>>>>>>> {self.cleaned_data}')

        correct_answers = 0

        for i in range(self.limit):

            user_answer = self.cleaned_data.get(f'question{i}')

            if user_answer is None:
                print(self.questions[i])
                print(self.cleaned_data.get(f'question{i}'))

            if user_answer.is_valid:
                correct_answers += 1

        self.cleaned_data['correct_answers'] = correct_answers



