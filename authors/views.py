from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.contrib.auth import get_user_model
from .serializer import AuthorsSerializer
from .models import AuthorsModel

# Create your views here.
class AuthorsModelViewSet(ModelViewSet):
    # user = get_user_model()
    queryset = AuthorsModel.objects.all()
    serializer_class = AuthorsSerializer