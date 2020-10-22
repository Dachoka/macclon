from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Image(models.Model):
    image = ImageField(blank=True, manual_crop="")
    name = models.CharField(max_length = 80)
    caption = models.TextField(blank = True)
    profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE, null = True)
    photo = ImageField(blank=True, manual_crop="")
    bio = models.TextField(default = "No bio available...", blank = True)

    def save_profile(self):
        self.save()

    def update_profile(self, new_bio):
        self.update(bio = new_bio)

    def delete_profile(self):
        self.delete()

    def profile_posts(self):
        pass

    def __str__(self):
        return self.bio

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
    image = models.ForeignKey('Image', on_delete = models.CASCADE, related_name = 'usercomments')
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['date_added']

    def save_comment(self):
        self.save()

    def update_comment(self, new_content):
        self.update(content = new_content)

    def delete_comment(self):
        self.delete()

    def __str__(self):
        return self.content
    