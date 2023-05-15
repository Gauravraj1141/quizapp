from rest_framework.views import APIView
from rest_framework.response import Response
from quizapp.models import  Quiz, QuizQuestion, QuizAnswer, QuizStatus
from quizapp.serializers import QuizSerializer, QuizQuestionSerializer, QuizAnswerSerializer, QuizStatusSerializer


class QuizResult(APIView):
  
  def get(self,request,id):
        try:
            quiz = Quiz.objects.get(quiz_id=id)
            finished_quiz_result_data = {}
            if str(quiz.status) == "finished":
                    quiz_questions = QuizQuestion.objects.filter(quiz=id)
                    quiz_question_serializer = QuizQuestionSerializer(quiz_questions, many=True)
                    score = 0
                    for question in quiz_question_serializer.data:
                        score  += question['question_marks']
                    finished_quiz_result_data['Score'] = f"{score}/{score}"
            else:
                finished_quiz_result_data['status'] = "Quiz is not finished wait for sometime"

            payload = [{'status':200,'payload':finished_quiz_result_data}]
            return Response(payload)
        except Exception as e:
            return Response({"exception":str(e)})