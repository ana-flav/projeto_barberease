from django.urls import path

from .views import LoginView, ClienteCadastrarView

app_name = "pessoa"

#URLs para o app pessoa
urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("cadastrar/", ClienteCadastrarView.as_view(), name="cadastro"),
]