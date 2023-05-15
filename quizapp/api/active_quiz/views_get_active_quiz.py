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
                    active_quiz_data.append(quiz)
            payload = [{'status':200,'data':active_quiz_data}]
            return Response(payload)
        except Exception as e:
            return Response({"exception":str(e)})