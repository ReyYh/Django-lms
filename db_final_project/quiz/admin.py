from django.contrib import admin
from .models import Type, Question, Quiz, Choice, Answer, Result


admin.site.register(Type)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(Result)
