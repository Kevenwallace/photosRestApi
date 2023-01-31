from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.
class Photos (models.Model):
    user = get_user_model()
    titulo = models.CharField(max_length=250)
    descricao = models.TextField("")
    imagem = models.ImageField()
    autor = models.ForeignKey(user, on_delete=models.CASCADE)