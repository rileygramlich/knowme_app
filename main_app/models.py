from django.db import models
from django.contrib.auth.models import User

QUESTIONS = (
    ('1', 'What is my favorite color?'), 
    ('2', 'What is my favourite food?'),
    ('3', 'What is my favourite animal?'), 
    ('4', 'What is my favourite movie?'), 
    ('5', 'Who is my favourite music artist?'), 
)


# Create your models here.
class Quiz(models.Model):
    user: models.ForeignKey(User, on_delete=models.CASCADE)
    name: models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    user: models.ForeignKey(User, on_delete=models.CASCADE)
    quiz: models.ForeignKey(Quiz, on_delete=models.SET_NULL)
    question: models.CharField(
        max_length=1,
        choices=QUESTIONS,
        default=QUESTIONS[0][0]
    )
    true_answer: models.CharField(max_length=250)
    false_answer1: models.CharField(max_length=250)
    false_answer2: models.CharField(max_length=250)
    false_answer3: models.CharField(max_length=250)

    def __str__(self):
        return self.id


# QnAns Model

# Question Form Model