from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.template import Context, Template
from django.utils.safestring import mark_safe

# Create your models here.


class Chapter(models.Model):
    id = models.PositiveIntegerField(primary_key=True)

    title = models.CharField(max_length=100, null=False)
    image = models.ImageField(default='chapter_default.png', upload_to='chapter_pics')
    description = models.CharField(max_length=100, null=True, blank=True,
                                   default='This is a sample description for chapter, contact your local admin for changing it.')
    # This should be html code
    body = models.TextField(null=False)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, null=False)

    extra_material = models.CharField(max_length=100, null=False, blank=True, default='https://www.google.com',
                                      help_text='This SHOULD be url link to extra studying material for the current chapter!')

    def __str__(self):
        return self.name


class StatisticsPerCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    answers_total = models.PositiveIntegerField(default=0)
    answers_correct = models.PositiveIntegerField(default=0)
    answers_wrong = models.PositiveIntegerField(default=0)

    bad_at = models.BooleanField(default=False)

    def __str__(self):
        return f'Category: {self.category} for User: {self.user}'


class Questionnaire(models.Model):
    id = models.PositiveIntegerField(primary_key=True)

    name = models.CharField(max_length=100, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='questionnaire', on_delete=models.CASCADE)

    def __str__(self):
        return f'Quiz: {self.name}'


class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, related_name='questions', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    prompt = models.CharField(max_length=100, null=False)
    show = models.BooleanField(default=True, help_text='Whether to show question in questionnaire or not')

    def __str__(self):
        return self.prompt


class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, related_name='question_answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100, null=False)
    is_valid = models.BooleanField()

    def __str__(self):
        return f'{self.answer} for "{self.question}"'


class Statistics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)

    times_read = models.PositiveIntegerField(default=0)
    times_taken = models.PositiveIntegerField(default=0)
    answers_total = models.PositiveIntegerField(default=0)
    answers_correct = models.PositiveIntegerField(default=0)
    answers_wrong = models.PositiveIntegerField(default=0)
    success_rate = models.FloatField(default=0.0)

    passed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}, for {self.questionnaire}'


