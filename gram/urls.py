from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django_filters.views import FilterView

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('signup/', views.signup, name = 'signup'),
    path('upload/',views.uploadphoto, name ='upload'),
    path('profile/', views.profile, name = 'profile'),
    path('addprofile/', views.addprofile, name = 'addprofile'),
    path('explore/', views.explore, name = 'explore'),
    path('about/', views.about, name = 'about'),
    path('imagefilter/', views.filterimage, name = 'filterimage'),
    path('profilefilter/', views.filterprofile, name = 'filterprofile'),
    path('image/<int:image_id>/',views.imagedetail, name ='imagedetail'),
    path('addcomment/<int:image_id>/',views.addcomment, name ='addcomment'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


