from rest_framework import serializers
from .models import Photos

class PhotosSeralizer(serializers.ModelField):
    class Meta:
        model = Photos
        fieds = '__all__'