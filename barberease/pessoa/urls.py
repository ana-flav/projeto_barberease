from django.urls import path

from .views import LoginView, ClienteCadastrarView, ClienteHomeView 
from django.contrib.auth.views import  LogoutView
app_name = "pessoa"
from django.contrib.auth.decorators import login_required
#URLs para o app pessoa
urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("cadastrar/", ClienteCadastrarView.as_view(), name="cadastro"),
    path("home/", login_required(ClienteHomeView.as_view()), name="home"),
    path("logout/", LogoutView.as_view(), name="logout"),
]