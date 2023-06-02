from django.contrib import admin

# Register your models here.
from core.models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'created_at', 'data_uploaded')
    search_fields = ('id', 'created_at', 'data_uploaded')


admin.site.register(Question, QuestionAdmin)
