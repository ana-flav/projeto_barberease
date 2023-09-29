from django.urls import path

from .views import LoginView, ClienteCadastrarView, ClienteHomeView, ClienteLogoutView

app_name = "pessoa"

#URLs para o app pessoa
urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("cadastrar/", ClienteCadastrarView.as_view(), name="cadastro"),
    path("home/", ClienteHomeView.as_view(), name="home"),
    path("logout/", ClienteLogoutView.as_view(), name="logout"),
]