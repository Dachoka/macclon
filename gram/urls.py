from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('signup/', views.signup, name = 'signup'),
    path('upload/',views.uploadphoto, name ='upload'),
    path('profile/', views.profile, name = 'profile')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)