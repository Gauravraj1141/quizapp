from rest_framework.views import APIView
from rest_framework.response import Response
from quizapp.models import  Quiz, QuizQuestion, QuizAnswer, QuizStatus
from quizapp.serializers import QuizSerializer, QuizQuestionSerializer, QuizAnswerSerializer, QuizStatusSerializer


class ActiveQuiz(APIView):
  
  def get(self,request):
        try:
            quiz_data  = Quiz.objects.all()
            quiz_serializer = QuizSerializer(quiz_data, many=True)
            active_quiz_data = []
            for quiz in quiz_serializer.data:
                    if quiz['status'] == 2:
                        question_data = QuizQuestion.objects.filter(quiz = quiz['quiz_id'])
                        question_serializer = QuizQuestionSerializer(question_data, many=True)
                        quiz['question'] = question_serializer.data
                        quiz['status'] = "Active"
                        for answer in question_serializer.data:
                            answer_data = QuizAnswer.objects.filter(question = answer['question_id'])
                            answer_serializer = QuizAnswerSerializer(answer_data, many=True)
                            answer['answer'] = answer_serializer.data
                        active_quiz_data.append(quiz)
            if len(active_quiz_data) == 0:
                active_quiz_data.append("There is no Active Quiz , please try again later!")

            payload = [{'status':200,'data':active_quiz_data}]
            return Response(payload)
        except Exception as e:
            return Response({"exception":str(e)})