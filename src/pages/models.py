from django.db import models

# Create your models here.


class FrequentlyAskedQuestion(models.Model):

    title = models.CharField(max_length=100, null=False, blank=False)
    body = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.title

