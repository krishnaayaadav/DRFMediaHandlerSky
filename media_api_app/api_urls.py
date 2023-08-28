from .api_views import VideoAPI, AudioAPI
from django.urls import path

urlpatterns = [
   path('videos/', VideoAPI.as_view(), name='all_videos'),
   path('audios/', AudioAPI.as_view(), name='all_videos'),

]