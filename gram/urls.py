from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('signup/', views.signup, name = 'signup'),
    path('upload/',views.uploadphoto, name ='upload'),
    path('profile/', views.profile, name = 'profile'),
    path('addprofile/', views.addprofile, name = 'addprofile'),
    path('explore/', views.explore, name = 'explore'),
    path('about/', views.about, name = 'about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


