from rest_framework import serializers
from .models import Photos

class PhotosSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = '__all__'