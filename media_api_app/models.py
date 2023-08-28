from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
   name = models.CharField(max_length=200)

   def __str__(self):
      return self.name

class Video(models.Model):
   videofile   = models.FileField(upload_to='Videos/')
   title       = models.CharField(max_length=200)
   description = models.TextField(blank=True, null=True)
   category    = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='videos')
   created     = models.DateField(auto_now_add=True) 
   updated     = models.DateField(auto_now=True)
   creator     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_videos')

   def __str__(self):
      return f'{self.title} | {self.creator.username}'
