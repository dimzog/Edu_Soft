from django.contrib import admin
from .models import Questionnaire, Question, UserAnswer, QuestionAnswer


# Register your models here.

admin.site.register(Questionnaire)
admin.site.register(Question)
admin.site.register(QuestionAnswer)
admin.site.register(UserAnswer)
