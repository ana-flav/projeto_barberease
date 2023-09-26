from django.contrib.auth.views import LoginView
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Cliente
from .forms import ClienteForm  

class UsuarioLoginView(LoginView):
    # Views para renderizar a tela inicial Usuario

    template_name = "login.html"
    success_url = reverse_lazy("pessoa:cadastro")

class ClienteCadastrarView(CreateView):
    # Views para renderizar a tela de cadastro de Cliente

    form_class = ClienteForm  
    template_name = "cliente_cadastro.html"
    model = Cliente
    success_url = reverse_lazy("pessoa:login")

        



