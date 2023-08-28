from django.urls import path
from media_api_app import api_views 
urlpatterns = [
   path('videos/', api_views.VideoAPI.as_view(), name='all_videos'),
   path('videos/<int:video_pk>/', api_views.VideoDetials.as_view(), name='video_details'),

   path('audios/', api_views.AudioAPI.as_view(), name='all_videos'),
   path('audios/<int:audio_pk>/', api_views.AudioDetials.as_view(), name='audio_details'),


]