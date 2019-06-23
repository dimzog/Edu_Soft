from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Quiz(models.Model):

    chapter = models.PositiveIntegerField(null=False)
    description = models.TextField(max_length=150, null=False, default='')

    def __str__(self):
        return f'Revision Quiz for Chapter: {self.chapter}'
    

class Question(models.Model):

    title = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=150, null=False)
    category = models.CharField(max_length=50, default='Syntax', null=False)

    choice_a = models.CharField(max_length=50, null=False, default='')
    choice_b = models.CharField(max_length=50, null=False, default='')
    choice_c = models.CharField(max_length=50, null=False, default='')
    choice_d = models.CharField(max_length=50, null=False, default='')

    answer = models.CharField(max_length=50, null=False, default='')

    test = models.ManyToManyField(Quiz)

    def __str__(self):
        return f'Type: {self.category}, Title: "{self.title}".'


