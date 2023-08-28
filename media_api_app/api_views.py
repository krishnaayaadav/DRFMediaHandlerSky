
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .models import Video, Audio
from .serializers import VideoSerializer, AudioSerializer

# get all videos api
class VideoAPI(generics.ListAPIView):
    
   queryset = Video.objects.all()
   serializer_class = VideoSerializer

   def get_queryset(self):
      return Video.objects.all()
    
# get all audios api
class AudioAPI(generics.ListAPIView):
    
   queryset = Audio.objects.all()
   serializer_class = AudioSerializer

   def get_queryset(self):
      return Audio.objects.all()
    
  