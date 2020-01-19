from django import template
from ..models import Person,Paroquia,Encontro,Membros,Equipe
from django.http import HttpRequest
from django.template.defaultfilters import stringfilter

register = template.Library()

# @register.filter
@stringfilter
def busca_equipe(value):
    try:
        equipe =  Membros.objects.all().values('equipe__nome_equipe').get(person_id=value)

    except Membros.DoesNotExist:
        equipe = None

    if equipe != None:
        return equipe['equipe__nome_equipe']
    else:
        return 'sem equipe'


@stringfilter
def busca_status_equipe(value):
    aux=""
    try:
        status =  Membros.objects.all().values('status_conv').get(person_id=value)
        aux = str(status['status_conv'])
    except Membros.DoesNotExist:
        status = "Sem Status"
    
    if aux == 'a':
         status = 'Aceito'
    elif aux == 'ac':
        status = 'Aguardando Envio'
    elif aux == 'e':
        status = 'Enviado'
    elif aux == 'r':
        status = 'Recusado'
    elif aux == 'd':   
        status = 'Desistiu'       
    else :
        status = 'Sem Retorno'
    
    return status

register.filter('busca_equipe', busca_equipe)
register.filter('busca_status_equipe', busca_status_equipe)