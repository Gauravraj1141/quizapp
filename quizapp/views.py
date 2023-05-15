# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import *
# from .serializers import QuizSerializer, AnswerSerializer


# class CreateQuiz(APIView):
#     def get(self,request):
#         try:
#             data  = Quiz.objects.all()
#             serialize_data = QuizSerializer(data, many=True)
#             for question in serialize_data.data:
#                 answer_data = QuizAnswer.objects.filter(question = question['quiz_id'])
#                 answer_serializer = AnswerSerializer(answer_data, many=True)
#                 question['answer'] = answer_serializer.data
#             payload = [{'status':200,'data':serialize_data.data}]
#             print(payload)
#             # return Response(payload)
#         except Exception as e:
#             return Response(e)