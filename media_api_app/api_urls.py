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
   path('audios/<int:audio_pk>/', api_views.AudioDetials.as_view(), name='audio_details'),
   path('audios/update/<int:audio_pk>/', api_views.UpdateAudioAPI.as_view(), name='update_audio'),
   path('audios/delete/<int:audio_pk>/', api_views.DeleteAudioAPI.as_view(), name='delete_audio'),




]