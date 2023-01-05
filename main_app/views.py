from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import QUESTIONS, Quiz, Question

questions = Question.objects.all()

# AUTH PAGES 
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/quizzes')
    else:
      error_message = 'Invalid credentials - try again'
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
    'quizzes': Quiz.objects.all(),
    'questions': questions,
    'quiz': Quiz
  })

def quizzes_detail(request, quiz_id):
  quiz = Quiz.objects.get(id=quiz_id)
  questions = Question.objects.all()
  questions_quiz_doesnt_have = Question.objects.exclude(id__in = quiz.questions.all().values_list('id'))
  print(questions_quiz_doesnt_have.all())
  return render(request, 'quizzes/detail.html', {
  'quiz': quiz,
  'questions': questions,
  'questions_quiz_doesnt_have': questions_quiz_doesnt_have
  })
    
class QuizCreate(CreateView):
  model = Quiz
  fields = ['name']
  success_url = '/quizzes/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class QuizUpdate(UpdateView):
  model = Quiz
  fields = ['name']

class QuizDelete(DeleteView):
  model = Quiz
  success_url = '/quizzes/'

def quiz_take_quiz(request, quiz_id):
  quiz = Quiz.objects.get(id=quiz_id)
  return render(request, 'main_app/quiz_take_quiz.html', {
    'quiz': quiz
    })

# QUESTION PATHS
class QuestionCreate(LoginRequiredMixin, CreateView):
  model = Question
  fields = ['question', 'true_answer', 'false_answer1', 'false_answer2', 'false_answer3']
  success_url = '/quizzes/'

  def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def question_new(request):
  form = request.POST
  print(form['question'])
  QUESTIONS.append([(len(QUESTIONS) + 1), form['question']])
  print(QUESTIONS)
  return redirect('question_create')

class QuestionUpdate(LoginRequiredMixin, UpdateView):
  model = Question

class QuestionDelete(DeleteView):
  model = Question
  success_url = '/quizzes/'

def assoc_question(request, quiz_id, question_id):
  Quiz.objects.get(id=quiz_id).questions.add(question_id)
  print(question_id)
  return redirect('detail', quiz_id=quiz_id)

def unassoc_question(request, quiz_id, question_id):
  Quiz.objects.get(id=quiz_id).questions.remove(question_id)
  print(question_id)
  return redirect('detail', quiz_id=quiz_id)