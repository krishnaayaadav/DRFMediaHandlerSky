
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

#  video detials or get single/detail video
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
      
#  video update 
class UpdateVideoAPI(APIView):

   def patch(self, request, video_pk,  format=None):

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

         serializer = VideoSerializer(instance=video, data=request.data, partial=True)
         if serializer.is_valid(raise_exception=True):
            serializer.save()

            response = {
               'msg': f'Congrats! Video of pk: {video_pk} successfully updated',
               'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
         else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  delete video 
class DeleteVideoAPI(APIView):

   def delete(self, request, video_pk,  format=None):
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
         video.delete()
         response = {
            'msg': f'Video delete successfully of pk: {video_pk}',
         }
         return Response(response, status=status.HTTP_204_NO_CONTENT)

# get all audios api
class AudioAPI(generics.ListAPIView):
    
   queryset = Audio.objects.all()
   serializer_class = AudioSerializer

   def get_queryset(self):
      return Audio.objects.all()

#  Audio detials or get single/detail Audio
class AudioDetials(APIView):

   def get(self, request, audio_pk,  format=None):
      error_response = {
         'non_found_error': f'No Audio found with this pk:  {audio_pk}'
      }
      try:
         audio = Audio.objects.get(pk = audio_pk)

      except Audio.DoesNotExist:
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      except Audio.MultipleObjectsReturned:
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      except :
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      else:

         serializer = AudioSerializer(audio)
         response = {
            'msg': f'Detial of Audio of pk: {audio_pk}',
            'data': serializer.data
         }
         return Response(response, status=status.HTTP_200_OK)

#  Audio detials or get single/detail Audio
class UpdateAudioAPI(APIView):

   def patch(self, request, audio_pk,  format=None):
      error_response = {
         'non_found_error': f'No Audio found with this pk: {audio_pk}'
      }
      try:
         audio = Audio.objects.get(pk = audio_pk)

      except Audio.DoesNotExist:
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      except Audio.MultipleObjectsReturned:
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      except :
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      else:

         serializer = AudioSerializer(instance=audio, data=request.data, partial=True)
         if serializer.is_valid(raise_exception=True):
            serializer.save()
               
            response = {
               'msg': f'Congrats! Audio of pk: {audio_pk} updated successfully',
               'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
         else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
#  Audio detials or get single/detail Audio
class DeleteAudioAPI(APIView):

   def delete(self, request, audio_pk,  format=None):
      error_response = {
         'non_found_error': f'No Audio found with this pk:  {audio_pk}'
      }
      try:
         audio = Audio.objects.get(pk = audio_pk)

      except Audio.DoesNotExist:
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      except Audio.MultipleObjectsReturned:
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      except :
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      else:

         audio.delete()
         response = {
            'msg': f'Audio deleted successfully of pk: {audio_pk}',
         }
         return Response(response, status=status.HTTP_204_NO_CONTENT)
      
