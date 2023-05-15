from django.urls import path
from quizapp.api.show_quiz.views_show_quiz import ShowQuiz
from quizapp.api.create_quiz.views_create_quiz import CreateQuiz
from quizapp.api.active_quiz.views_get_active_quiz import ActiveQuiz
from quizapp.api.quiz_result.view_quiz_result import QuizResult

urlpatterns = [
    path('/', CreateQuiz.as_view()),
    path('all/', ShowQuiz.as_view(), name='all'),
    path('active/', ActiveQuiz.as_view(), name='active'),
    path('<uuid:id>/result/', QuizResult.as_view(), name='result'),

]