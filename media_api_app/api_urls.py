from django.urls import path
from media_api_app import api_views 
urlpatterns = [
   # videos api here
   path('videos/', api_views.VideoAPI.as_view(), name='all_videos'),
   path('videos/detail/<int:video_pk>/', api_views.VideoDetials.as_view(), name='video_details'),
   path('videos/update/<int:video_pk>/', api_views.UpdateVideoAPI.as_view(), name='update_video'),
   path('videos/delete/<int:video_pk>/', api_views.DeleteVideoAPI.as_view(), name='delete_video'),

   # audios api here
   path('audios/', api_views.AudioAPI.as_view(), name='all_videos'),
   path('audios/detial/<int:audio_pk>/', api_views.AudioDetials.as_view(), name='audio_details'),
   path('audios/update/<int:audio_pk>/', api_views.UpdateAudioAPI.as_view(), name='update_audio'),
   path('audios/delete/<int:audio_pk>/', api_views.DeleteAudioAPI.as_view(), name='delete_audio'),

   # pdf files api endpoints here
   path('pdf-files/', api_views.PDFFilesAPI().as_view(), name='get_all_pdf_files'),
   path('pdf-files/detail/<int:pdf_pk>/', api_views.PDFFileDetials().as_view(), name='pdf_detials'),
   path('pdf-files/update/<int:pdf_pk>/', api_views.UpdatePDFfilesPI().as_view(), name='update_pdf_files'),
   path('pdf-files/delete/<int:pdf_pk>/', api_views.DeletePDFfilesAPI().as_view(), name='delete_pdf_files'),

]