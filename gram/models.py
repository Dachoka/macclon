from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/')
    name = models.CharField(max_length = 80)
    caption = models.TextField()
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    likes = models.IntegerField()
    comments = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True, null = True)


