from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate,logout
from .forms import UserCreateForm,UploadPhotoForm
from .email import send_welcome_email
from django.conf import settings

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def signup(request):
    form = UserCreateForm()

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")

            send_welcome_email(user,email)

    return render(request, 'registration/signup.html',{"form":form,})

def uploadphoto(request):
    form = UploadPhotoForm()
    current_user = request.user

    if request.method=='POST':
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            image.profile = current_user
            image.save()
            return redirect('home')
    
    else:
        form = UploadPhotoForm()
    return render(request, 'new_photo.html',{"form":form})
    


