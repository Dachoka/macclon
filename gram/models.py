from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/')
    name = models.CharField(max_length = 80)
    caption = models.TextField(blank = True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    likes = models.IntegerField(default = 0)
    comments = models.TextField(blank = True)
    upload_date = models.DateTimeField(auto_now_add=True, null = True)

    def save_image(self):
        self.save()

    def update_image(self):
        self.update()

    def delete_image(self):
        self.delete()


class Profile(models.Model):
    photo = models.ImageField(upload_to = 'photos/')
    bio = models.TextField()

    def save_profile(self):
        self.save()

    def update_profile(self):
        self.update()

    def delete_profile(self):
        self.delete()