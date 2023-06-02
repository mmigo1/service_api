from django.db import models


class Question(models.Model):
    id = models.IntegerField(verbose_name='ID вопроса', primary_key=True)
    question = models.TextField(max_length=200, verbose_name='Текст вопроса',null=True)
    answer = models.TextField(max_length=200, verbose_name='Ответ на вопрос',null=True)
    created_at = models.DateTimeField(verbose_name='Дата создания вопроса',null=True)
    data_uploaded = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки В БД', null=True)
