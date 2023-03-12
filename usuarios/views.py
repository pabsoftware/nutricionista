from django.shortcuts import render, redirect
from django.http import HttpResponse
from . utils import senha_e_valida
from . models import CustomUser
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

# Create your views here.

def cad_usuario(request):
    if request.method == 'GET':
        template_name = 'cadastro_use.html'
    if request.method == 'POST':
        template_name = 'cadastro_use.html'
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        if not senha_e_valida(request, senha, confirmar_senha):
            return redirect('cadastrar')
        try:
            user = CustomUser.objects.create_user(
                                            username    = usuario,
                                            email       =email,
                                            password    = senha,
                                            is_active   = False)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Cadastrado com sucesso')
            return redirect('cadastrar')
        except:
            messages.add_message(request, constants.ERROR, 'Houve um erro ao tentar cadastrar. Tente mais tarde.')
            return redirect('cadastrar')

    
    return render(request, template_name)
    


def login(request):
    if request.method == 'GET':
        template_name = 'login.html'
    if request.method == 'POST':
        template_name = 'login.html'
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=usuario, password=senha)
        if not user:
            messages.add_message(request, constants.ERROR, ' Usuário ou senha iválido')
            return redirect('login')
        else:
            auth.login(request, user)
            return HttpResponse('logado com sucesso')
    return render(request, template_name)
