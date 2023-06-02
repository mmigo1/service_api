from django.urls import path
from rest_framework import routers

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('api/', question_api, name='api'),
]
