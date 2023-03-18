from django.urls import path
from . views import pacientes, dados_paciente_listar, dados_paciente

urlpatterns = [
    path('pacientes/', pacientes, name='pacientes'),
    path('dados_paciente/', dados_paciente_listar, name='dados_paciente_listar'),
    path('dados_paciente/<str:id>/', dados_paciente, name='dados_paciente')

    
]