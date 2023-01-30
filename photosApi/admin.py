from django.contrib import admin
from .models import Photos

# Register your models here.
class PhotosAdmin(admin.ModelAdmin):
    ...
    
admin.site.register(Photos, PhotosAdmin)