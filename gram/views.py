from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate,logout
from .forms import UserCreateForm,UploadPhotoForm,UpdateProfileForm
from .email import send_welcome_email
from django.conf import settings
from .models import Image,Profile
from django.contrib.auth.models import User


# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def signup(request):

    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        profile_form = UpdateProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user =user_form.save()
            profile = profile_form.save(commit =False)
            profile.user = request.user
            profile.save()
            username = user_form.cleaned_data.get("username")
            email = user_form.cleaned_data.get("email")

            send_welcome_email(username,email)
            return redirect('profile')

    else:
        user_form = UserCreateForm()

    return render(request, 'registration/signup.html',{"user_form":user_form,"profile_form":profile_form})

def addprofile(request):
    form = UpdateProfileForm()
    current_user = request.user

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit = False)
            profile.owner = current_user
            profile.save()
            return redirect ('profile')
        else:
            form = UpdateProfileForm()
    return render(request, 'photos/new_pic.html', {"form":form})


def uploadphoto(request):
    form = UploadPhotoForm()
    current_user = request.user

    if request.method=='POST':
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
            return redirect('home')
    
    else:
        form = UploadPhotoForm()
    return render(request, 'photos/new_photo.html',{"form":form})


   


