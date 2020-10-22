from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image,Profile,Comment


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(max_length = 100, help_text = 'Required')
    class Meta:
        model = User
        fields = ['username','email', 'password1','password2']

class UploadPhotoForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile','likes','comments','upload_date']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo','bio']

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

