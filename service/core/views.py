from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
import requests

from rest_framework.decorators import api_view

from core.models import Question
from core.serializers import QuestionSerializer


def request_quest(number: int):
    url: str = f'https://jservice.io/api/random?count={number}'
    response = requests.get(url)
    return response.json()


def add_question(questions_number: int):
    for quest in request_quest(questions_number):
        id: int = quest['id']
        try:
            question_obj: object = Question.objects.get(pk=id)
        except ObjectDoesNotExist:
            question_obj: None = None
        if question_obj:
            add_question(1)
            continue
        question: str = quest['question']
        answer: str = quest['answer']
        created_at = quest['created_at']
        serializer = QuestionSerializer(
            data={'id': id, 'question': question, "answer": answer, 'created_at': created_at})
        if serializer.is_valid():
            serializer.save()


@api_view((['GET', 'POST']))
def question_api(request):
    if request.method == 'GET':
        try:
            question_last: object = Question.objects.latest("data_uploaded")
            serializer: object = QuestionSerializer(question_last, many=False)
            return Response({'Последний сохранённый вопрос викторины': serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        try:
            if type(int(request.data['questions_num'])) is not 'int':
                return Response(['Введён неверный тип данных'], status=status.HTTP_400_BAD_REQUEST)
            questions_number: int = request.data['questions_num']
        except:
            return Response(['Введён неверный тип данных'], status=status.HTTP_400_BAD_REQUEST)
        add_question(questions_number)
        question_last: object = Question.objects.latest("data_uploaded")
        serializer = QuestionSerializer(question_last, many=False)
        return Response({'Последний сохранённый вопрос викторины': serializer.data}, status=status.HTTP_201_CREATED)

    return Response({'Ошибка, повторите'}, status=status.HTTP_400_BAD_REQUEST)
