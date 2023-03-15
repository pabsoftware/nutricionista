import re
from django.contrib import messages
from django.contrib.messages import constants

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

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



def email_html(path_template: str, assunto: str, para: list, **kwargs) -> dict:
    html_content = render_to_string(path_template, kwargs)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(assunto, text_content, settings.EMAIL_HOST_USER, para)
    email.attach_alternative(html_content, "text/html")
    email.send()
    return {'status': 1}
