from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Photos
from .serializer import PhotosSeralizer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import get_object_or_404
from .permissions import IsOwner



# Create your views here.
class PhotosModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Photos.objects.all()
    serializer_class = PhotosSeralizer

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(
            self.get_queryset(),
            pk=pk
        )
        self.check_object_permissions(self.request, obj)
        return obj
    
    
    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE' ]:
            return[IsOwner(), ]
        return super().get_permissions()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(autor=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
    
    def get_queryset(self):
        qr = super().get_queryset()
        autor = self.request.query_params.get('autor', None)
        if autor is not None:
            qr = qr.filter(autor=autor)
        id = self.request.query_params.get('id', None)
        if id is not None:
            qr = qr.filter(id=id)
        return qr