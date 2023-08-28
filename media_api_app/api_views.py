
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .models import Video
from .serializers import VideoSerializer

class VideoAPI(generics.ListAPIView):
    
   queryset = Video.objects.all()
   serializer_class = VideoSerializer

   def get_queryset(self):
      return Video.objects.all()
    
  