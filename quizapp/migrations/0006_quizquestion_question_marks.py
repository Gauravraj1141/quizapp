# Generated by Django 4.2.1 on 2023-05-14 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0005_alter_quiz_quiz_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizquestion',
            name='question_marks',
            field=models.IntegerField(default=5),
        ),
    ]