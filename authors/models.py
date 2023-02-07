from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class AuthorsModel(AbstractUser):
    REQUIRED_FIELDS = [ 'first_name', 'last_name' ]
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=8)
    email = models.EmailField(max_length=250, unique=True, error_messages={'unique': "O email cadastrado já existe."})
    fullname = models.CharField(max_length=250)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'