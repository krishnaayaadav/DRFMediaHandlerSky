from .api_views import VideoAPI
from django.urls import path

urlpatterns = [
   path('videos/', VideoAPI.as_view(), name='all_videos'),
]