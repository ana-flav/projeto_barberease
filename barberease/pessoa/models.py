from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from allauth.account.signals import user_logged_in
from allauth.socialaccount.models import SocialAccount
from django.shortcuts import redirect

# class Empresa(models.Model):
#     pass

# class Barbeiro(models.Model):
#     pass

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField("Nome", max_length=150)
    sobrenome = models.CharField("Sobrenome", max_length=150, null=True, blank=True)
    email = models.EmailField("E-mail", unique=True, null=True, blank=True)


    def __str__(self):
        return self.user | self.user
    
@receiver(post_save, sender=User)
def signal_create_cliente(sender, instance, created, **kwargs):
    if created:
        Cliente.objects.create(user=instance, email=instance.email, nome=instance.first_name, sobrenome=instance.last_name)

@receiver(user_logged_in)
def custom_user_logged_in(sender, request, user, **kwargs):
    social_account = SocialAccount.objects.filter(user=user, provider='google').first()

    if social_account is None:
        return redirect('pessoa:cadastro')