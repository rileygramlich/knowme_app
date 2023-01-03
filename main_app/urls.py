from django.urls import path, include
from . import views

urlpatterns = [

    #Authorization
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    #App
    path('', views.home, name='home'),
    #Quiz
    path('quiz/', views.quiz_form_index, name='quiz_form_index'),
    path('quizzes/<int:quiz_id>', views.quizzes_detail, name='detail'),
    #Question
    path('questions/create/', views.QuestionsCreate.as_view(), name='questions_create'),
    path('questions/<int:pk>/update/', views.QuestionsUpdate.as_view(), name='questions_update'),
    path('questions/<int:pk>/delete/', views.QuestionsDelete.as_view(), name='questions_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
]