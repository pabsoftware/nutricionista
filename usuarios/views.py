from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . utils import senha_e_valida, email_html
from . models import CustomUser, Ativacao
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth
import os
from django.conf import settings
from hashlib import sha256

# Create your views here.

def cad_usuario(request):
    if request.method == 'GET':
        template_name = 'cadastro_use.html'
        if request.user.is_authenticated:
            return redirect('/')
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

            token = sha256(f"{usuario} {email}".encode()).hexdigest()
            ativacao = Ativacao(token=token, user=user)
            ativacao.save()
            path_template = os.path.join(settings.BASE_DIR, 'usuarios/templates/email/cadastro_confirmado.html')
            email_html(path_template, 'Cadastro confirmado', [email,], username = usuario, link_ativacao = f"127.0.0.1:8000/auth/ativacao/{token}")
            messages.add_message(request, constants.SUCCESS, 'Cadastrado com sucesso. Acesse seu email e clique no link para ativar seu cadastro')
            return redirect('cadastrar')
        except:
            messages.add_message(request, constants.ERROR, 'Houve um erro ao tentar cadastrar. Tente mais tarde.')
            return redirect('cadastrar')

    
    return render(request, template_name)
    


def login(request):
    if request.method == 'GET':
        template_name = 'login.html'
        if request.user.is_authenticated:
            return redirect('/')
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
            return redirect('pacientes')
    return render(request, template_name)


def logout(request):
    auth.logout(request)
    return redirect('login')

def ativar_conta(request, token):
    token = get_object_or_404(Ativacao, token = token)
    if token.ativo:
        messages.add_message(request, constants.WARNING, 'Essa token ja foi usado')
        return redirect('login')
    user = CustomUser.objects.get(username = token.user.username)
    user.is_active = True
    user.save()
    token.ativo = True
    token.save()
    messages.add_message(request, constants.SUCCESS, 'Conta ativada com sucesso')
    return redirect('login')
    
    return redirect('/')
