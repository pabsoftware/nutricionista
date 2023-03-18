from django.contrib import admin
from . models import Pacientes, DadosPaciente
# Register your models here.
admin.site.register(Pacientes)
admin.site.register(DadosPaciente)