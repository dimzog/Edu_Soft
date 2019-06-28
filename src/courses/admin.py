from django.contrib import admin
from .models import Questionnaire, Question, QuestionAnswer, Statistics, Chapter, StatisticsPerCategory, Category


# Register your models here.

admin.site.register(Questionnaire)
admin.site.register(Question)
admin.site.register(QuestionAnswer)


admin.site.register(Category)


admin.site.register(Statistics)
admin.site.register(StatisticsPerCategory)


admin.site.register(Chapter)



