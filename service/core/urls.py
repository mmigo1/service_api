from django.urls import path

from .views import *

urlpatterns = [
    path('question', question_api, name='api'),
]
