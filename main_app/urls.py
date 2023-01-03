from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    #Quiz
    path('quiz/', views.quiz_form_index, name='quiz_form_index'),
    path('quizzes/<int:quiz_id>', views.quizzes_detail, name='detail'),
    path('quizzes/create', views.QuizCreate.as_view(), name='quiz_create'),
    path('quizzes/<int:pk>/update', views.QuizUpdate.as_view(), name='quiz_update'),
    path('quizzes/<int:pk>/delete/', views.QuizDelete.as_view(), name='quiz_delete'),
    path('quizzes/<int:quiz_id>/take', views.quiz_take_quiz, name='quiz_take_quiz'),
    #Question
    path('questions/create/', views.QuestionsCreate.as_view(), name='questions_create'),
    path('questions/<int:pk>/update/', views.QuestionsUpdate.as_view(), name='questions_update'),
    path('questions/<int:pk>/delete/', views.QuestionsDelete.as_view(), name='questions_delete'),
    path('accounts/signup/', views.signup, name='signup'),

]