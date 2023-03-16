from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def pacientes(request):
    template_name = 'plataforma/paciente.html'
    return render(request, template_name)