from django.urls import path, include
from . import views

urlpatterns = [
    #Authorization
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    #App
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #Quiz
    path('quizzes/', views.quizzes_index, name='index'),
    path('quizzes/<int:quiz_id>/', views.quizzes_detail, name='detail'),
    path('quizzes/create/', views.QuizCreate.as_view(), name='quiz_create'),
    path('quizzes/<int:pk>/update', views.QuizUpdate.as_view(), name='quiz_update'),
    path('quizzes/<int:pk>/delete/', views.QuizDelete.as_view(), name='quiz_delete'),
    path('quizzes/take/<int:quiz_id>/', views.quiz_take_quiz, name='quiz_take_quiz'),
    #Question
    path('questions/create/', views.QuestionCreate.as_view(), name='question_create'),
    path('questions/<int:pk>/update/', views.QuestionUpdate.as_view(), name='question_update'),
    # path('questions/<int:pk>/delete/', views.QuestionDelete.as_view(), name='question_delete'),
]