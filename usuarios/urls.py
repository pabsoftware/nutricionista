from django.urls import path
from .views import cad_usuario, login, logout, ativar_conta

urlpatterns = [
    path('cadastro/', cad_usuario, name = 'cadastrar'),
    path('login/', login, name = 'login' ),
    path('logout/', logout, name = 'logout' ),
    path('ativacao/<str:token>/', ativar_conta, name='ativar_conta')

]