import re
from django.contrib import messages
from django.contrib.messages import constants

def senha_e_valida(request, senha, confirma_senha):
    if len(senha) < 6:
        messages.add_message(request, constants.WARNING, 'Sua senha deve ter pelo menos 6 caracters')
        return False
    
    if not senha == confirma_senha:
        messages.add_message(request, constants.WARNING, 'A senhas não coincidem ')
        return False
    
    if not re.search('[A-Z]', senha):
        messages.add_message(request, constants.WARNING, 'Sua senha não contem letras maiusculas')
        return False
    
    if not re.search('[a-z]', senha):
        messages.add_message(request, constants.WARNING, 'Sua senha não contem letras minusculas')
        return False
    
    if not re.search('[1-9]', senha):
        messages.add_message(request, constants.WARNING, 'Sua senha não contem letras números')
        return False
    
    return True