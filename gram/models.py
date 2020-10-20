from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = ImageField(blank=True, manual_crop="")
    name = models.CharField(max_length = 80)
    caption = models.TextField(blank = True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default = 0)
    comments = models.TextField(blank = True)
    upload_date = models.DateTimeField(auto_now_add=True, null = True)

    def save_image(self):
        self.save()

    def update_caption(self, new_caption):
        self.update(caption = new_caption)

    def delete_image(self):
        self.delete()

    @classmethod
    def get_all_images(cls):
        all_images = cls.objects.all()
        return all_images



class Profile(models.Model):
    owner = models.OneToOneField(User,on_delete = models.CASCADE, null = True)
    photo = ImageField(blank=True, manual_crop="")
    bio = models.TextField()

    def save_profile(self):
        self.save()

    def update_profile(self, new_bio):
        self.update(bio = new_bio)

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.owner.username