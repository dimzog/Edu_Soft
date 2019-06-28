from django import forms
from .models import Questionnaire, QuestionAnswer, Question, StatisticsPerCategory
from django.contrib.auth.models import User
from django.db import models


class TestForm(forms.Form):

    limit = 0
    user = None

    def __init__(self, *args, **kwargs):
        chapter = kwargs.pop('chapter')
        self.limit = kwargs.pop('limit')
        super(TestForm, self).__init__(*args, **kwargs)
#
        # Grab Questionnaire for current Chapter
        self.questionnaire = Questionnaire.objects.get(id=chapter)
#
        # self.questions = self.questionnaire.questions.order_by('?').all()[:self.limit]
        self.questions = self.questionnaire.questions.filter(show=True)

        # Trim then down if more than recommended limit
        if self.limit < len(self.questions):
            self.questions = self.questions[:self.limit]

        # Change select class, because of faulty css
        widget = forms.Select(attrs={'class': 'browser-default'})
#
        # Create question for number of limit, change limit to add more
        for counter, q in enumerate(self.questions):
            if q.show:
                self.fields[f'question{counter}'] = forms.ModelChoiceField(label=q,
                                                                           queryset=QuestionAnswer.objects.filter(question=q,
                                                                                                                  question__questionnaire=self.questionnaire),
                                                                           required=True,
                                                                           # to_field_name='answer',
                                                                           empty_label=None,
                                                                           widget=widget
                                                                           )

    #def clean(self):
    #    correct_answers = 0
#
    #    for i in range(self.limit):
#
    #        user_answer = self.cleaned_data.get(f'question{i}')
#
    #        if user_answer.is_valid:
    #            correct_answers += 1
#
    #    self.cleaned_data['correct_answers'] = correct_answers



