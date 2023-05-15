from django.contrib import admin

from .models import *

admin.site.register(QuizStatus)
admin.site.register(Quiz)
admin.site.register(QuizAnswer)
admin.site.register(QuizQuestion)