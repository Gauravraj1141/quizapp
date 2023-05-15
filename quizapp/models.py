from django.db import models
import uuid
from datetime import datetime

class QuizStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.status)

class Quiz(models.Model):
    quiz_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
    quiz_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(QuizStatus, on_delete=models.CASCADE, default=1)
    start_date = models.DateTimeField(default = datetime.now, null= True)
    end_date = models.DateTimeField(default = datetime.now, null= True)
    
    def __str__(self) -> str:
        return str(self.quiz_id)
    
class QuizQuestion(models.Model):
    question_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,related_name='question_quiz')
    question_text = models.CharField(max_length=1000)
    question_marks = models.IntegerField(default=5)

    def __str__(self) -> str:
        return str(self.question_id)


class QuizAnswer(models.Model):
    answer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE , related_name='question_answer')
    answer = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return str(self.answer_id)
