import django_filters
from .models import Image,Profile
from django.contrib.auth.models import User


class ImageFilter(django_filters.FilterSet):
    class Meta:
        model = Image
        fields = {'name': ['icontains'], 'caption':['icontains','profile__username':['icontains']]}