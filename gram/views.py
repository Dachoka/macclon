from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
from .email import send_welcome_email

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def signup(request):
    form = UserCreateForm()

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'registration/signup.html',{"form":form,})

