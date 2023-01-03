from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #Quiz
    path('quizzes/', views.quizzes_index, name='index'),
    path('quizzes/<int:quiz_id', views.quizzes_detail, name='detail'),
    #Question
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('/test', views.test_form_index, name='test_form_index')

]