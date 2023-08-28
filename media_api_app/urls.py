from django.urls import path, include
from .views import homepage

urlpatterns = [
   path('', homepage, name='homepage'),

   # api urls/endpoints
   path('api/', include('media_api_app.api_urls'))
   
]