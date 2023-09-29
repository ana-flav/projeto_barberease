from collections.abc import Mapping
from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Cliente

class ClienteForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput) 
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Cliente
        exclude = ['user']
    
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['password2'].label = 'Confirmação de senha'

    # def clean(self):
    # Método para validar os campos do formulário 
    #  TODO:FAZER VERIFICAÇÃO DE SENHA

    def save(self, commit=True):
        """Criar um novo usuario django para o meu cliente"""
        instance = super().save(commit=False)
        usuario = User.objects.create_user(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )
        instance.user = usuario
        instance.save()
        return instance
    

class ClienteForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput) 
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Cliente
        exclude = ['user']
    
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['password2'].label = 'Confirmação de senha'

    # def clean(self):
    # Método para validar os campos do formulário 
    #  TODO:FAZER VERIFICAÇÃO DE SENHA

    def save(self, commit=True):
        """Criar um novo usuario django para o meu cliente"""
        instance = super().save(commit=False)
        usuario = User.objects.create_user(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )
        instance.user = usuario
        instance.save()
        return instance