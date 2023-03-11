from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cad_usuario(request):

    return HttpResponse('Você está na página de cadstro de usuario')


def login(request):

    return HttpResponse('você está na tela de login')
