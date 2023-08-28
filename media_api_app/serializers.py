
from .models import Video, UserProfile
from rest_framework import serializers

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model  = User
      fields = ('username', 'first_name', 'last_name')

class UserProfileSerializer(serializers.ModelSerializer):
   user  = UserSerializer()
   class Meta:
      model  = UserProfile
      fields = ('user','about_user', 'profession',  'profile_img')

class VideoSerializer(serializers.ModelSerializer):
   creator = UserProfileSerializer()
   category = serializers.StringRelatedField()
   
    
   class Meta:
      model  = Video
      fields = ('pk', 'title', 'thumnail','videofile', 'description', 'category', 'created', 'updated', 'creator')
        