from django.urls import path
from .views import cad_usuario, login

urlpatterns = [
    path('cadastro/', cad_usuario, name = 'cadastrar'),
    path('login/', login, name = 'login' ),
]