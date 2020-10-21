from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate,logout
from .forms import UserCreateForm,UploadPhotoForm,UpdateProfileForm
from .email import send_welcome_email
from django.conf import settings
from .models import Image,Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def profile(request):
    current_user = request.user
    return render(request, 'profile.html')

def explore(request):
    images = Image.objects.all()
    profiles = Profile.objects.all()
    current_user = request.user
    return render(request, 'explore.html',{'images':images,'profiles':profiles,'user':current_user})

def signup(request):


    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        if user_form.is_valid():
            user =user_form.save(commit = False)
            username = user_form.cleaned_data.get("username")
            email = user_form.cleaned_data.get("email")
            password1 = user_form.cleaned_data.get("password1")
            password2 = user_form.cleaned_data.get("password2")
            new_user = User.objects.create(username =username, email=email, password = password1)
            new_user.save()
            login(request,new_user)

            send_welcome_email(username,email)
            return redirect('addprofile')

    else:
        user_form = UserCreateForm()

    return render(request, 'registration/signup.html',{"user_form":user_form})

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


   


