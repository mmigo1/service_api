from rest_framework import serializers

from core.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'answer', 'created_at')
