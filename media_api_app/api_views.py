
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Video, Audio, PDFfile
from .serializers import VideoSerializer, AudioSerializer, PDFFileSerializer

from drf_spectacular.utils import extend_schema

####### Audio API Here #########

# get all videos api
@extend_schema(summary='Get All Video files')
class VideoAPI(generics.ListAPIView):
    
   queryset = Video.objects.all()
   serializer_class = VideoSerializer

   def get_queryset(self):
      return Video.objects.all()

#  video detials or get single/detail video
@extend_schema(summary='Get Single/Detial Of VideoFiles')
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

@extend_schema(summary='Update VideoFiles')
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

@extend_schema(summary='Delete VideoFile')
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

####### Audio API Here #########

# get all audios api
@extend_schema(summary='Get All Audio Files')
class AudioAPI(generics.ListAPIView):
    
   queryset = Audio.objects.all()
   serializer_class = AudioSerializer

   def get_queryset(self):
      return Audio.objects.all()

#  Audio detials or get single/detail Audio
@extend_schema(summary='Get Detial/Single Audio File')
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
@extend_schema(summary='Update Audio Files')
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
@extend_schema(summary='Delete Audio Files')
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
      
####### PDFfiles API Here #########


# get all PDFfiles 
@extend_schema(summary='Get All PDF Files')
class PDFFilesAPI(generics.ListAPIView):
    
   queryset = PDFfile.objects.all()
   serializer_class = PDFFileSerializer

   def get_queryset(self):
      return PDFfile.objects.all()

#  PDFfiles detials or get single/detail PDFfiles
@extend_schema(summary='Get Detial/Single PDF File')
class PDFFileDetials(APIView):

   def get(self, request, pdf_pk,  format=None):
      error_response = {
         'non_found_error': f'No PDFfiles found with this pk:  {pdf_pk}'
      }
      try:
         pdf_file = PDFfile.objects.get(pk = pdf_pk)

      except PDFfile.DoesNotExist:
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      except PDFfile.MultipleObjectsReturned:
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      except :
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      else:

         serializer = PDFFileSerializer(pdf_file)
         response = {
            'msg': f'Detial of PDF of pk: {pdf_pk}',
            'data': serializer.data
         }
         return Response(response, status=status.HTTP_200_OK)

#  Update PDFfiles 
@extend_schema(summary='Update PDF Files')
class UpdatePDFfilesPI(APIView):

   def patch(self, request, pdf_pk,  format=None):
      error_response = {
         'non_found_error': f'No PDFfiles found with this pk: {pdf_pk}'
      }
      try:
         pdf_file = PDFfile.objects.get(pk = pdf_pk)

      except PDFfile.DoesNotExist:
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      except PDFfile.MultipleObjectsReturned:
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      except :
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      else:

         serializer = PDFFileSerializer(instance=pdf_file, data=request.data, partial=True)
         if serializer.is_valid(raise_exception=True):
            serializer.save()
               
            response = {
               'msg': f'Congrats! PDFfile of pk: {pdf_pk} updated successfully',
               'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
         else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
# delete  PDFfiles 
@extend_schema(summary='Delete PDF Files')
class DeletePDFfilesAPI(APIView):

   def delete(self, request, pdf_pk,  format=None):
      error_response = {
         'non_found_error': f'No PDFfiles found with this pk:  {pdf_pk}'
      }
      try:
         pdf_file = Audio.objects.get(pk = pdf_pk)

      except PDFfile.DoesNotExist:
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      except PDFfile.MultipleObjectsReturned:
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      except :
         return Response(error_response, status=status.HTTP_404_NOT_FOUND)
      
      else:

         pdf_file.delete()
         response = {
            'msg': f'PDF deleted successfully of pk: {pdf_pk}',
         }
         return Response(response, status=status.HTTP_204_NO_CONTENT)
      