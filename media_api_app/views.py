from django.shortcuts import render

from .models import Video, PDFfile

def homepage(request):
   all_videos = Video.objects.all()
   all_pdf    = PDFfile.objects.all()
   context    ={
      'all_videos': all_videos,
      'all_pdfs': all_pdf
   }
   return render(request, 'home.html', context)
