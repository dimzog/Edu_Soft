from django.contrib import admin
from .models import Questionnaire, Question, QuestionAnswer, Statistics, Chapter


# Register your models here.

admin.site.register(Questionnaire)
admin.site.register(Question)
admin.site.register(QuestionAnswer)


admin.site.register(Statistics)


admin.site.register(Chapter)



