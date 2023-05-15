from django.urls import path
from quizapp.api.show_quiz.views_show_quiz import ShowQuiz
from quizapp.api.create_quiz.views_create_quiz import CreateQuiz

urlpatterns = [
    path('/', CreateQuiz.as_view()),
    path('all/', ShowQuiz.as_view(), name='all')

]