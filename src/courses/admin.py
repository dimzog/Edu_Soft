from django.contrib import admin
from .models import Questionnaire, Question, UserQuestionnaire


# Register your models here.

admin.site.register(Questionnaire)
admin.site.register(Question)
admin.site.register(UserQuestionnaire)