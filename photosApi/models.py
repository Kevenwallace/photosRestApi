from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Photos (models.Model):
    titulo = models.CharField(max_length=250)
    descricao = models.TextField("")
    imagem = models.ImageField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)