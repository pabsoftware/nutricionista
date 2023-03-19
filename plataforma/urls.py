from django.urls import path
from . views import pacientes, dados_paciente_listar, dados_paciente, grafico_peso, plano_alimentar_listar, plano_alimentar, refeicao, Opcao

urlpatterns = [
    path('pacientes/', pacientes, name='pacientes'),
    path('dados_paciente/', dados_paciente_listar, name='dados_paciente_listar'),
    path('dados_paciente/<str:id>/', dados_paciente, name='dados_paciente'),
    path('grafico_peso/<str:id>/', grafico_peso, name="grafico_peso"),
    path('plano_alimentar/', plano_alimentar_listar, name='plano_alimentar_listar'),
    path('plano_alimentar/<str:id>/', plano_alimentar, name='plano_alimentar'),
    path('refeicao/<str:id_paciente>/', refeicao, name='refeicao'),

    
]