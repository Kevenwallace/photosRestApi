from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import AuthorsModel, AbstractUser
import re
from django.core.exceptions import ValidationError



class AuthorsSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only= True,
        label= 'digite sua senha'
    )
    
    password_confirm = serializers.CharField(
        style= {'input_type': 'password'},
        write_only= True,
        label= 'confirme sua senha'
    )
    
    email = serializers.CharField(
        label= "digite seu email"
    )
    
    email = serializers.CharField(
        label= "digite seu email"
    )
    
    class Meta:
        model = AuthorsModel
        fields = (
            'id',
            'username',
            'password',
            'password_confirm',
            'email',
        )

    def save(self):
        conta = AuthorsModel(
            email=self.validated_data['email'], 
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password == password_confirm:
            regenx = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!-/:-@[-`{-~]).{8,}$')
            if not regenx.match(password):
                raise serializers.ValidationError({'password':'senha muito facil, sua senha deve conter pelo menos uma letra minuscula, uma maiuscula, um numero, um caractere especial e no minimo 8 digitos'})
        else:
            raise serializers.ValidationError({'password': 'As senhas não são iguais.'})
        conta.set_password(password)
        conta.save()
        return conta