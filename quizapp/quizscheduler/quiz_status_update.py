from apscheduler.schedulers.background import BackgroundScheduler
from quizapp.models import Quiz
from quizapp.serializers import QuizSerializer
from datetime import datetime



def update_quiz_status():
    all_quiz_data = Quiz.objects.all()
    serializer = QuizSerializer(all_quiz_data, many=True)
    for quiz_data in serializer.data:
        start_date = quiz_data['start_date']
        end_date = quiz_data['end_date']

        # Define the input and output format strings
        input_format = "%Y-%m-%dT%H:%M:%SZ"
        output_format = "%Y-%m-%d %H:%M:%S.%f"

        # Parse the input datetime string using strptime
        parsed_start_date = datetime.strptime(start_date, input_format)
        parsed_end_date = datetime.strptime(end_date, input_format)

        # Convert the parsed datetime to the desired format using strftime
        start_datetime = parsed_start_date.strftime(output_format)
        end_datetime = parsed_end_date.strftime(output_format)

        now = datetime.now()
        if start_datetime <= str(now) and end_datetime >= str(now):
            Quiz.objects.filter(quiz_id = quiz_data['quiz_id']).update(status=2)
           
        elif end_datetime < str(now):
            Quiz.objects.filter(quiz_id = quiz_data['quiz_id']).update(status=3)
            


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_quiz_status , 'interval',seconds = 1)
    scheduler.start()