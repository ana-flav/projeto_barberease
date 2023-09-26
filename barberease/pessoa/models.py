from django.db import models
from django.contrib.auth.models import User

# class Empresa(models.Model):
#     pass

# class Barbeiro(models.Model):
#     pass

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField("Nome", max_length=150)
    sobrenome = models.CharField("Sobrenome", max_length=150)
    email = models.EmailField("E-mail", unique=True, null=True, blank=True)


    def __str__(self):
        return self.user | self.user