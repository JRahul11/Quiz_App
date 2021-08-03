from django.contrib import admin
from quizapp.models import Answer, Question, Quizzes, Attempt


admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Quizzes)
admin.site.register(Attempt)
