from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.contrib.auth import get_user_model
from .serializer import AuthorsSerializer
from .models import AuthorsModel
from django.shortcuts import get_object_or_404
# Create your views here.
class AuthorsModelViewSet(ModelViewSet):
    # user = get_user_model()
    queryset = AuthorsModel.objects.all()
    serializer_class = AuthorsSerializer
    
    
    def get_object(self):
        # pk = self.kwargs.get('pk')
        obj = get_object_or_404(
            self.get_queryset(),
            pk=self.request.user.id
        )
        return obj