from django.urls import path
from . import views

urlpatterns = [
    # authentication
    path('accounts/signup/', views.signup, name='signup'),
    path('/test', views.test_form_index, name='test_form_index')
]