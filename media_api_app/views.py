from django.shortcuts import render

from .models import Video

def homepage(request):
   all_videos = Video.objects.all()
   return render(request, 'home.html', {'all_videos': all_videos})
