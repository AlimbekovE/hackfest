from django.db import models

# Create your models here.


class QuizName(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name}'


class Question(models.Model):
    question = models.CharField(max_length=64)
    url = models.CharField(max_length=64)
    quizName = models.ForeignKey(QuizName)

    def __str__(self):
        return f'{self.question}'
