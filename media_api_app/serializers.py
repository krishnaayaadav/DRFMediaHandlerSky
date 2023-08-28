
from .models import Video, UserProfile, Audio
from rest_framework import serializers

from django.contrib.auth.models import User

# user serializer
class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model  = User
      fields = ('username', 'first_name', 'last_name')

# user profile serializer
class UserProfileSerializer(serializers.ModelSerializer):
   user  = UserSerializer()
   class Meta:
      model  = UserProfile
      fields = ('user','about_user', 'profession',  'profile_img')

# video serializer
class VideoSerializer(serializers.ModelSerializer):
   creator = UserProfileSerializer()
   category = serializers.StringRelatedField()
   
    
   class Meta:
      model  = Video
      fields = ('pk', 'title', 'thumnail','videofile', 'description', 'category', 'created', 'updated', 'creator')


# video serializer
class AudioSerializer(serializers.ModelSerializer):
   creator = UserProfileSerializer()
   category = serializers.StringRelatedField()
   
    
   class Meta:
      model  = Audio
      fields = ('pk', 'title', 'thumnail','audiofile', 'description', 'category', 'created', 'updated', 'creator')
        