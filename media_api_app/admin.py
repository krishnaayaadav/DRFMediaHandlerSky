from django.contrib import admin
from .models import Category, Video, UserProfile, Audio

# category model added into django admin panel
@admin.register(Category)
class CategoryModel(admin.ModelAdmin):
   list_display = ('pk', 'name')

   search_fields = ('name', )

# video model  added into django admin panel
@admin.register(Video)
class VideoModel(admin.ModelAdmin):
   list_display = ('title', 'creator', 'category', 'created', 'updated', 'description', 'videofile')

   search_fields = ('title','creator', 'category' )

# auido model added into django admin panel
@admin.register(Audio)
class VideoModel(admin.ModelAdmin):
   list_display = ('title', 'creator', 'category', 'created', 'updated', 'description', 'audiofile')

   search_fields = ('title','creator', 'category' )

# user profile model added into django admin panel
@admin.register(UserProfile)
class UserProfileModel(admin.ModelAdmin):
   list_display = ('user', 'about_user', 'profession', 'profile_img')