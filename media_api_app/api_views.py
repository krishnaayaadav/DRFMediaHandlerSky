
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Video, Audio
from .serializers import VideoSerializer, AudioSerializer

# get all videos api
class VideoAPI(generics.ListAPIView):
    
   queryset = Video.objects.all()
   serializer_class = VideoSerializer

   def get_queryset(self):
      return Video.objects.all()

# complete video detials or get single/detail video
class VideoDetials(APIView):

   def get(self, request, video_pk,  format=None):
      error_response = {
         'non_found_error': f'No Video found with this {video_pk}'
      }
      try:
         video = Video.objects.get(pk = video_pk)

      except Video.DoesNotExist:
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      except Video.MultipleObjectsReturned:
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      except :
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      else:

         serializer = VideoSerializer(video)
         response = {
            'msg': f'Detial of Video of pk: {video_pk}',
            'data': serializer.data
         }
         return Response(response, status=status.HTTP_200_OK)
      

# get all audios api
class AudioAPI(generics.ListAPIView):
    
   queryset = Audio.objects.all()
   serializer_class = AudioSerializer

   def get_queryset(self):
      return Audio.objects.all()
    
  