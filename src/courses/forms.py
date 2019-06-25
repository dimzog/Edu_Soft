from django import forms
from .models import Questionnaire, QuestionAnswer
from django.contrib.auth.models import User
from django.db import models


class TestForm(forms.Form):

    limit = 5
    chapter = 'Chapter 1'

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)

        # Grab Questionnaire for current Chapter
        quest = Questionnaire.objects.select_related().get(version=self.chapter)

        # Grab questions that are foreign keys to current Questionnaire from database, limit them.
        qs = quest.questions.order_by('?').all()[:self.limit]

        print('\n')

        for q in qs:
            print(f'--- Question: {q}')
            for a in q.question_answer.all():
                print(f'Answer: {a} [x]') if a.is_valid else print(f'Answer: {a}')

        # Create question for number of limit, change limit to add more
        for counter, q in enumerate(qs):
            self.fields[f'question{counter}'] = forms.ModelChoiceField(label=q,
                                                                       queryset=q.question_answer.all(),
                                                                       to_field_name='answer',
                                                                       required=True,
                                                                       widget=forms.Select(
                                                                           attrs={'class': 'browser-default'})
                                                                       )

