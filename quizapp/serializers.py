from .models import *
from rest_framework import serializers


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = "__all__"

class QuizStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizStatus
        fields = "__all__"

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = "__all__"

class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswer
        fields = "__all__"