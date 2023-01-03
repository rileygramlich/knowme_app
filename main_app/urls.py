from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #Quiz
    path('quiz/', views.quiz_form_index, name='quiz_form_index'),
    path('quizzes/<int:quiz_id>', views.quizzes_detail, name='detail'),
    #Question
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
]