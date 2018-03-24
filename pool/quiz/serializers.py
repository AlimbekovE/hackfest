from rest_framework.serializers import ModelSerializer
from .models import QuizName, Question


class QuizNameSerializer(ModelSerializer):
    class Meta:
        model = QuizName
        fields = ('id', 'name')


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'quizName', 'question', 'url')
