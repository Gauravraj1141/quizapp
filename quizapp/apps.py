from django.apps import AppConfig


class QuizappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quizapp'

    def ready(self):
        print("start our sch suceefully..........")
        from .quizscheduler import quiz_status_update 
        quiz_status_update.start()
