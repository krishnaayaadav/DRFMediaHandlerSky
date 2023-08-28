from django.db import models
from django.contrib.auth.models import User

# user profile model
class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
   profile_img = models.ImageField(upload_to='User/images')
   about_user  = models.TextField(blank=True, null=True)
   profession  = models.CharField(max_length=100)

# category  model
class Category(models.Model):
   name = models.CharField(max_length=200)

   def __str__(self):
      return self.name
# video model
class Video(models.Model):
   thumnail    = models.ImageField(upload_to='Videos/thumbnals', blank=True, null=True)
   videofile   = models.FileField(upload_to='Videos/')
   title       = models.CharField(max_length=200)
   description = models.TextField(blank=True, null=True)
   category    = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='videos')
   created     = models.DateField(auto_now_add=True) 
   updated     = models.DateField(auto_now=True)
   creator     = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_videos')

   def __str__(self):
      return f'{self.title} '

# audio model
class Audio(models.Model):
   thumnail    = models.ImageField(upload_to='Audios/thumbnals', blank=True, null=True)
   audiofile   = models.FileField(upload_to='Audios/')
   title       = models.CharField(max_length=200)
   description = models.TextField(blank=True, null=True)
   category    = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='audio')
   created     = models.DateField(auto_now_add=True) 
   updated     = models.DateField(auto_now=True)
   creator     = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_audio')
   

