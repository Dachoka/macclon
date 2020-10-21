from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate,logout
from .forms import UserCreateForm,UploadPhotoForm,UpdateProfileForm,AddCommentForm
from .email import send_welcome_email
from django.conf import settings
from .models import Image,Profile,Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .filters import ImageFilter,ProfileFilter


# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(owner = current_user)
    images = Image.objects.filter(profile = current_user)
    return render(request, 'profile.html', {"user":current_user, "profile":profile, "images":images})

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
            return redirect('profile')
    
    else:
        form = UploadPhotoForm()
    return render(request, 'photos/new_photo.html',{"form":form})

def filterimage(request):
    if request is None:
        return Image.objects.none()
    filter_list = Image.objects.all()
    image_filter = ImageFilter(request.GET, queryset = filter_list)
    return render (request, 'searchimage.html', {"filter": image_filter})

def filterprofile(request):
    if request is None:
        return Profile.objects.none()
    filter_list = Profile.objects.all()
    profile_filter = ProfileFilter(request.GET, queryset = filter_list)
    return render (request, 'searchprofile.html', {"filter": profile_filter})

def image_detail(request, slug):
    image = get_object_or_404(Image, slug=slug)
    comments = image.usercomments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = AddCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.image = image
            new_comment.save()

        else:
            comment_form = AddCommentForm()

    return render(request, 'imagedetails.html',{'image':image,'comments':comments,'new_comment':new_comment,'comment_form':comment_form})





   


