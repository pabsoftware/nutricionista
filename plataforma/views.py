from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.contrib import messages
from . models import Pacientes, DadosPaciente
from datetime import datetime
# Create your views here.


@login_required(login_url='login')
def pacientes(request):
    template_name = 'plataforma/paciente.html'
    if request.method == 'GET':
        pacientes_list = Pacientes.objects.filter(nutri = request.user)
        return render(request, template_name, {'pacientes' : pacientes_list})
  
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sexo = request.POST.get('sexo')
        idade = request.POST.get('idade')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        #validando
        if (len(nome.strip()) == 0) or (len(sexo.strip()) == 0) or (len(idade.strip()) == 0) or (len(email.strip()) == 0) or (len(telefone.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Favor, preencha todos os campos')
            return redirect('/pacientes/')
       
        if not idade.isnumeric():
            messages.add_message(request, constants.ERROR, 'Favor, informe uma idade válida')
            return redirect('/pacientes/')
        
        paciente = Pacientes.objects.filter(email=email)

        if paciente.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um paciente com esse E-mail')
            return redirect('/pacientes/')
      
        # salvando os dados
        try:
            paciente1 = Pacientes.objects.create(
                nome    =nome,
                sexo    =sexo,
                idade   =idade,
                email   =email,
            telefone =telefone, nutri=request.user )
            paciente1.save()
            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucsso')
            return redirect('/pacientes/')
        except:
            messages.add_message(request, constants.ERROR, 'Houve um erro ao cadastrar paciente')
            return redirect('/pacientes/')

@login_required(login_url='login')       
def dados_paciente_listar(request):
    template_name = 'plataforma/dados_pacientes_listar.html'
    pacientes = Pacientes.objects.filter(nutri=request.user)
    return render(request, template_name, {'pacientes':pacientes})


def dados_paciente(request, id):
    template_name = 'plataforma/dados_paciente.html'
    paciente = get_object_or_404(Pacientes, id=id)
    if not paciente.nutri == request.user:
        messages.add_message(request, constants.ERROR, 'Esse paciente não é seu')
        return redirect('/dados_paciente/')
    if request.method == 'GET':
        dados_pac= DadosPaciente.objects.filter(paciente=id)
       
        return render(request, template_name, {'paciente':paciente, 'dados_paciente':dados_pac})
    elif request.method == "POST":
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')
        gordura = request.POST.get('gordura')
        musculo = request.POST.get('musculo')
        hdl = request.POST.get('hdl')
        ldl = request.POST.get('ldl')
        colesterol_total = request.POST.get('ctotal')
        triglicerídios = request.POST.get('triglicerídios')

       ## if peso or altura or gordura == '':
          #  messages.add_message(request, constants.ERROR, 'Prencha todos os campos')
           # return redirect('/dados_paciente/')
        
        paciente = DadosPaciente(paciente=paciente,
                                data=datetime.now(),
                                peso=peso,
                                altura=altura,
                                percentual_gordura=gordura,
                                percentual_musculo=musculo,
                                colesterol_hdl=hdl,
                                colesterol_ldl=ldl,
                                colesterol_total=colesterol_total,
                                trigliceridios=triglicerídios)
        paciente.save()
        messages.add_message(request, constants.SUCCESS, 'Dados cadastrado com sucesso')
        return redirect('/dados_paciente/')
        
