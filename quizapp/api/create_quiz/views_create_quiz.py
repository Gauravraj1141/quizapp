from rest_framework.views import APIView
from rest_framework.response import Response
from quizapp.models import Quiz, QuizQuestion, QuizAnswer
from quizapp.serializers import QuizSerializer, QuizQuestionSerializer, QuizAnswerSerializer
from datetime import datetime
from django.utils import timezone
import json


class CreateQuiz(APIView):

    def post(self, request):
        try:
            input_json = request.data
            start_date_obj = datetime.strptime(input_json['start_date'], '%d-%m-%Y %H,%M')
            start_date = start_date_obj.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            end_date_obj = datetime.strptime(input_json['end_date'], '%d-%m-%Y %H,%M')
            end_date = end_date_obj.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            create_quiz_params = {"quiz_name":input_json['quiz_name'],"start_date":start_date,"end_date":end_date}
            
            create_quiz_data = QuizSerializer(data=create_quiz_params)
            if create_quiz_data.is_valid():
                create_quiz_data.save()
            quiz_id = create_quiz_data.data['quiz_id']
            questions = input_json['questions']
            options = input_json['options']
            answers = input_json['answers']
            for i in range(len(questions)):
                question_params = {"question_text":questions[i],"quiz": quiz_id}
                create_questions_data = QuizQuestionSerializer(data = question_params)
                if create_questions_data.is_valid():
                    create_questions_data.save()
                create_quiz_data.data['question'] = create_questions_data.data
                answer = answers[i]
                for j in range(len(options[i])):
                    option_params = {"question":create_questions_data.data['question_id'],"answer": options[i][j],"is_correct":False}
                    if options[i][j] == options[i][answer]:
                        option_params['is_correct'] = True
                    create_options_data = QuizAnswerSerializer(data = option_params)
                    if create_options_data.is_valid():
                        create_options_data.save()
                    create_quiz_data.data['options'] = create_options_data.data
                    
            return Response(create_quiz_data.data)
        except Exception as e:
            return Response({"exception":str(e)})
