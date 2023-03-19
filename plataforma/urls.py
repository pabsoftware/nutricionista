from django.urls import path
from . views import pacientes, dados_paciente_listar, dados_paciente, grafico_peso

urlpatterns = [
    path('pacientes/', pacientes, name='pacientes'),
    path('dados_paciente/', dados_paciente_listar, name='dados_paciente_listar'),
    path('dados_paciente/<str:id>/', dados_paciente, name='dados_paciente'),
    path('grafico_peso/<str:id>/', grafico_peso, name="grafico_peso")

    
]