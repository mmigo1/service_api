from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
import requests

from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.request import Request
from core.models import Question
from core.serializers import QuestionSerializer

from django.http import HttpResponse


def request_quest(number: int):
    url = f'https://jservice.io/api/random?count={number}'
    response = requests.get(url)
    return response.json()


def add_question(questions_number: int):
    for x in request_quest(questions_number):
        id: int = x['id']
        try:
            question_obj: object = Question.objects.get(pk=id)
        except ObjectDoesNotExist:
            question_obj: None = None
        if question_obj:
            add_question(1)
            continue
        question: str = x['question']
        answer: str = x['answer']
        created_at = x['created_at']
        serializer = QuestionSerializer(
            data= {'id': id, 'question': question, "answer": answer, 'created_at': created_at})
        if serializer.is_valid():
            serializer.save()


@api_view((['GET', 'POST']))
def index(request):
    if request.method == 'POST':
        questions_number: int = request.POST.get("questions_num", 'Undefined')
        add_question(questions_number)
        try:
            return render(request=request, template_name='core/index.html',
                          context={'question': Question.objects.latest("data_uploaded")})
        except:
            return render(request=request, template_name='core/index.html')
    try:
        return render(request=request, template_name='core/index.html',
                      context={'question': Question.objects.latest("data_uploaded")})
    except:
        return render(request=request, template_name='core/index.html')


@api_view((['GET', 'POST']))
def question_api(request):
    if request.method == 'GET':
        try:
            question_last: object = Question.objects.latest("data_uploaded")
            serializer: object = QuestionSerializer(question_last, many=False)
            return Response({'Последний сохранённый вопрос викторины': serializer.data})
        except:
            return Response({})

    elif request.method == 'POST':
        try:
            questions_number: int = request.data['questions_num']
        except:
            return Response(['Введён неверный тип данных'],status=status.HTTP_400_BAD_REQUEST)
        questions_number: int = request.data['questions_num']
        add_question(questions_number)
        question_last: object = Question.objects.latest("data_uploaded")
        serializer: object = QuestionSerializer(question_last, many=False)
        return Response({'Последний сохранённый вопрос викторины': serializer.data}, status=status.HTTP_201_CREATED)
