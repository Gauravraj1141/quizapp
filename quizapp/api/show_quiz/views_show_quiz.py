from rest_framework.views import APIView
from rest_framework.response import Response
from quizapp.models import  Quiz, QuizQuestion, QuizAnswer, QuizStatus
from quizapp.serializers import QuizSerializer, QuizQuestionSerializer, QuizAnswerSerializer, QuizStatusSerializer


class ShowQuiz(APIView):

    def get(self,request):
        try:
            quiz_data  = Quiz.objects.all()
            quiz_serializer = QuizSerializer(quiz_data, many=True)
            for quiz in quiz_serializer.data:
                quiz_status = QuizStatus.objects.get(status_id = quiz['status'])
                quiz_data = QuizStatusSerializer(quiz_status)
                quiz['status'] = quiz_data.data['status']
                question_data = QuizQuestion.objects.filter(quiz = quiz['quiz_id'])
                question_serializer = QuizQuestionSerializer(question_data, many=True)
                quiz['question'] = question_serializer.data
                for answer in question_serializer.data:
                    answer_data = QuizAnswer.objects.filter(question = answer['question_id'])
                    answer_serializer = QuizAnswerSerializer(answer_data, many=True)
                    answer['answer'] = answer_serializer.data
            payload = [{'status':200,'data':quiz_serializer.data}]
            return Response(payload)
        except Exception as e:
            return Response({"exception":str(e)})