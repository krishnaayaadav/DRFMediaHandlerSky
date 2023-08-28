from django.contrib import admin
from .models import Category, Video, UserProfile

@admin.register(Category)
class CategoryModel(admin.ModelAdmin):
   list_display = ('pk', 'name')

   search_fields = ('name', )


@admin.register(Video)
class VideoModel(admin.ModelAdmin):
   list_display = ('title', 'creator', 'category', 'created', 'updated', 'description', 'videofile')

   search_fields = ('title','creator', 'category' )

@admin.register(UserProfile)
class UserProfileModel(admin.ModelAdmin):
   list_display = ('user', 'about_user', 'profession', 'profile_img')