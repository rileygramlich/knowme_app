from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import QUESTIONS,  Quiz, Question

# AUTH PAGES 
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
  
  
 # GENERAL PATHS 
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# QUIZ PATHS
def quizzes_index(request):
    return render(request, 'quizzes/index.html', {
    })

def quizzes_detail(request):
    return render(request, 'quizzes/detail.html', {
    'questions': QUESTIONS,
    'question': Question,
    'quiz': Quiz
    })
    
class QuizCreate(CreateView):
  model = Quiz

class QuizUpdate(UpdateView):
  model = Quiz

class QuizDelete(DeleteView):
  model = Quiz
  success_url = '/quizzes/index'

def quiz_take_quiz(request):
  return render(request, 'main_app/quiz_take_quiz.html', {
    'questions': QUESTIONS,
    'question': Question,
    'quiz': Quiz
    })

# QUESTION PATHS
