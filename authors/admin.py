from django.contrib import admin

# Register your models here.
from .models import AuthorsModel
from django.contrib.auth.admin import UserAdmin

admin.site.register(AuthorsModel, UserAdmin)