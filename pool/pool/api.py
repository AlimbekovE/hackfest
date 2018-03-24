from rest_framework.routers import DefaultRouter
from quiz.views import QuizNameViewSet, QuestionViewSet

from rest_framework_extensions.routers import NestedRouterMixin


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()

quizNames_router = router.register('quizes', QuizNameViewSet)
quizNames_router.register('questions', QuestionViewSet, base_name='quizName-questions', parents_query_lookups=['quizName'])


#router = DefaultRouter()

#router.register('quizes', QuizNameViewSet)
#router.register('questions', QuestionViewSet)
