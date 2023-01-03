from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


# GENERAL PATHS 
def home(request):
  return render(request, 'home.html')



# AUTH PAGES 
def signup(request):
  error_message = ''
  if request.method == 'POST': # if the user submited a form 
    form = UserCreationForm(request.POST) # Making a new instance of the class, request.POST is the body of the form
    if form.is_valid(): # Validate it
      user = form.save() # If valid, save
      login(request, user)
      return redirect('index') # Redirect to indec
    else:
      print(form.errors) #not valid
      error_message = form.errors # error message
  form = UserCreationForm() #empty form 
  return render(request, 'registration/signup.html', {
    'form': form,
    'error_message': error_message
  }) 

