
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm
from allauth.account.views import SignupView, LoginView, TemplateView, LogoutView
from allauth.socialaccount.views import SignupView




class UsuarioLoginView(LoginView):
    # Views para renderizar a tela inicial Usuario

    template_name = "login.html"
    success_url = reverse_lazy("pessoa:home")


class ClienteCadastrarView(SignupView):
    # Views para renderizar a tela de cadastro de Cliente

    form_class = ClienteForm  
    template_name = "account/signup.html"
    model = Cliente
    success_url = reverse_lazy("pessoa:home")


class ClienteHomeView(TemplateView):
    # Views para renderizar a tela inicial Cliente

    template_name = "cliente_home.html"
    success_url = reverse_lazy("pessoa:home")

