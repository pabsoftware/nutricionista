from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cad_usuario(request):
    template = 'cadastro.html'

    return render(request, template)


def login(request):

    return HttpResponse('você está na tela de login')
