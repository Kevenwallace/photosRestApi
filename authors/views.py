from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.contrib.auth import get_user_model
from .serializer import AuthorsSerializer
from .models import AuthorsModel
from django.shortcuts import get_object_or_404
# Create your views here.
class AuthorsModelViewSet(ModelViewSet):
    # user = get_user_model()
    serializer_class = AuthorsSerializer
    
    def get_queryset(self):
        user = AuthorsModel
        qs = user.objects.filter(username=self.request.user.username)
        print(self.request.user.username)
        return qs
    
    
   