from django.urls import path, include
from . import views

urlpatterns = [
    #Authorization
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    #App
    path('', views.home, name='home'),
    #Quiz
    path('quizzes', views.quizzes_index, name='quizzes/index'),
    path('quizzes/<int:quiz_id>', views.quizzes_detail, name='detail'),

    #Question
]