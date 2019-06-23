from django.db import models
from django.contrib.auth.models import User


# Create your models here.

from django.conf import settings
from django.db import models


class Question(models.Model):
    chapter = models.PositiveIntegerField(null=False)

    prompt = models.CharField(max_length=255, null=False)

    choice_a = models.CharField(max_length=50, null=False)
    choice_b = models.CharField(max_length=50, null=False)
    choice_c = models.CharField(max_length=50, null=False)
    choice_d = models.CharField(max_length=50, null=False)

    answer = models.CharField(max_length=50, null=False)

    category = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'Chapter {self.chapter}. Title: {self.prompt}'


class Questionnaire(models.Model):
    name = models.CharField(max_length=255)
    # A questionnaire can have many questions.
    # A question can be part of many questionnaires.
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return f'{self.name}'


class UserQuestionnaire(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)

    def __str__(self):
        return f'Quiz: {self.questionnaire}, created by {self.user}'


class UserResponse(models.Model):
    user_questionnaire = models.ForeignKey(UserQuestionnaire, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response_option = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f'User {self.user_questionnaire.user}, question: {self.question}'

