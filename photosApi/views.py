from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Photos
from .serializer import PhotosSeralizer

# Create your views here.
class PhotosModelViewSet(ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotosSeralizer
    
    
    def get_queryset(self):
        print(self)
        return super().get_queryset()
    