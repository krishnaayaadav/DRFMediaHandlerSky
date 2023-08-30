
from .models import Video, UserProfile, Audio, PDFfile
from rest_framework import serializers

from django.contrib.auth.models import User

# User serializer
class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model  = User
      fields = ('username', 'first_name', 'last_name')

# User Profile serializer
class UserProfileSerializer(serializers.ModelSerializer):
   user  = UserSerializer()
   class Meta:
      model  = UserProfile
      fields = ('user','about_user', 'profession',  'profile_img')

# Video serializer
class VideoSerializer(serializers.ModelSerializer):
   creator = UserProfileSerializer()
   category = serializers.StringRelatedField()
   
    
   class Meta:
      model  = Video
      fields = ('pk', 'title', 'thumnail','videofile', 'description', 'category', 'created', 'updated', 'creator')

# Audio serializer
class AudioSerializer(serializers.ModelSerializer):
   creator = UserProfileSerializer()
   category = serializers.StringRelatedField()
   
    
   class Meta:
      model  = Audio
      fields = ('pk', 'title', 'thumnail','audiofile', 'description', 'category', 'created', 'updated', 'creator')

# PDFfiles serializer
class PDFFileSerializer(serializers.ModelSerializer):
   creator = UserProfileSerializer()
   category = serializers.StringRelatedField()
   
    
   class Meta:
      model  = PDFfile
      fields = ('pk', 'title', 'creator', 'category', 'created', 'updated', 'description', 'pdf_file')
        