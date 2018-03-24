from rest_framework.viewsets import ModelViewSet
from .serializers import QuizNameSerializer, QuestionSerializer
from .models import QuizName, Question
from rest_framework_extensions.mixins import NestedViewSetMixin


class QuizNameViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = QuizNameSerializer
    queryset = QuizName.objects.all()


class QuestionViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
