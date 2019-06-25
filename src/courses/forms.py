from django import forms
from django.forms import ModelChoiceField, ModelMultipleChoiceField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Questionnaire, Question, QuestionAnswer


class TestForm(forms.Form):

    question1 = forms.ModelChoiceField(label='', queryset=QuestionAnswer.objects.none())
    question2 = forms.ModelChoiceField(label='', queryset=QuestionAnswer.objects.none())
    question3 = forms.ModelChoiceField(label='', queryset=QuestionAnswer.objects.none())
    question4 = forms.ModelChoiceField(label='', queryset=QuestionAnswer.objects.none())
    question5 = forms.ModelChoiceField(label='', queryset=QuestionAnswer.objects.none())

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)


        quest = Questionnaire.objects.select_related().get(version='Chapter 1')
        qs = quest.questions.order_by('?').all()[:5]
        print(f'\nFetching "{quest}": {5} random Questions for {5}.')
        for q in qs:
            print(f'--- Question: {q}')
            for a in q.question_answer.all():
                if a.is_valid:
                    print(f'Answer: {a} [x]')
                else:
                    print(f'Answer: {a}')


        self.fields['question1'] = forms.ModelChoiceField(label=qs[0], queryset=qs[0].question_answer.all(), to_field_name='answer', required=True,
                                                widget=forms.Select(attrs={'class': 'browser-default'}))

        self.fields['question2'] = forms.ModelChoiceField(label=qs[1], queryset=qs[1].question_answer.all(), to_field_name='answer', required=True,
                                               widget=forms.Select(attrs={'class': 'browser-default'}))

        self.fields['question3'] = forms.ModelChoiceField(label=qs[2], queryset=qs[2].question_answer.all(), to_field_name='answer', required=True,
                                               widget=forms.Select(attrs={'class': 'browser-default'}))

        self.fields['question4'] = forms.ModelChoiceField(label=qs[3], queryset=qs[3].question_answer.all(), to_field_name='answer', required=True,
                                               widget=forms.Select(attrs={'class': 'browser-default'}))

        self.fields['question5'] = forms.ModelChoiceField(label=qs[4], queryset=qs[4].question_answer.all(), to_field_name='answer', required=True,
                                           widget=forms.Select(attrs={'class': 'browser-default'}))




