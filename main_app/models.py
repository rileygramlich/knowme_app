from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



# QUESTIONS = [
#     ['1', 'What is my favorite color?'], 
#     ['2', 'What is my favourite food?'],
#     ['3', 'What is my favourite animal?'], 
#     ['4', 'What is my favourite movie?'], 
#     ['5', 'Who is my favourite music artist?'], 
# ]

# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=250)
    true_answer = models.CharField(max_length=250)
    false_answer1 = models.CharField(max_length=250)
    false_answer2 = models.CharField(max_length=250)
    false_answer3 = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.question}"

class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})
    




    
