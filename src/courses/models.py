from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

# Create your models here.


class Questionnaire(models.Model):
    version = models.CharField(max_length=100, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='questionnaire', on_delete=models.CASCADE)

    def __str__(self):
        return f'Quiz: {self.version}, created by {self.user}'


class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, related_name='questions', on_delete=models.CASCADE)
    prompt = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.prompt


class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, related_name='question_answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100, null=False)
    is_valid = models.BooleanField()

    def __str__(self):
        return self.answer


class UserAnswer(models.Model):
    answer = models.ForeignKey(QuestionAnswer, related_name='user_answer', on_delete=models.CASCADE)


