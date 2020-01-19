from django.shortcuts import render,redirect,get_object_or_404
from django.core import paginator
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http.response import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Equipe,Membros,Person

from .forms import newServoForm,newParoquiaForm,newEncontroForm

def lista_equipes(request):

    data = Membros.objects.all()
    list_equipe = list()
    list_membros=[5]
    for membro in data:
        
        servo  = Person.objects.get(id=membro.person_id)
        equipe_servo = Equipe.objects.get(id=membro.equipe_id) 

        if membro.status_conv == 'a':
            status = 'Aceito'
        elif membro.status_conv == 'ac':
            status = 'Aguardando Envio'
        elif membro.status_conv == 'e':
            status = 'Enviado'
        elif membro.status_conv == 'r':
            status = 'Recusado'
        elif membro.status_conv == 'd':   
            status = 'Desistiu'       
        else :
            status = 'Sem Retorno'

            
        list_membros = {'id'    : membro.id,
                         'nome'  : servo.nome,
                         'equipe': equipe_servo.nome_equipe,
                         'dt'    : str(membro.dt_convite),
                         'status': status,
                         'encontro': equipe_servo.encontro
                        }
                       
 
        list_equipe.append(list_membros)    
    if request.method == 'GET':                
        return render(request,'lista_equipes.html',{'equipes':list_equipe})


def listaEquipes1(request):
    serial = False    
    query = request.GET.get("busca",'')
    sort = request.GET.get("ordenar", '')
    page = request.GET.get("page", '')
    params = [serial,query,sort]

    try:
        equipes = consultaBanco(params)
        equipes = Paginator(equipes,20)#definindo a paginação
        equipes = equipes.page(page)
    except  PageNotAnInteger :
        equipes = equipes.page(1)
    except EmptyPage :
        equipes = paginator.page(paginator.num_page)

    if request.method == 'GET':        
        return render(request,'lista_equipes.html',{'equipes':equipes})
    else:
        return HttpResponse ("Logo faz algo")
    
def consultaBanco(params):
    if params[0] == True:
         data = serializers.serialize("json", Person.objects.all())
    elif params[1]:
         data = Equipe.objects.filter(nome__icontains = params[1])
    elif params[2]:
         data = Equipe.objects.all().order_by(params[2])     
    else:
         data = Equipe.objects.all()
    return data

def novaEquipe(request):
    form = newEquipeForm(request.POST or None, request.FILES or None)
   
    if form.is_valid():
        form.save()
        return redirect('lista_equipes')
    
    return render (request,'form_equipe.html',{'form': form})


def atualizaEquipe(request,id):
    equipe_object= get_object_or_404(Person,pk=id)
    form = newEquipeForm(request.POST or None,instance = equipe_object )
    if form.is_valid():
        form.save()
        return redirect('lista_equipes')

    return render (request,'form_equipe.html',{'form': form})
    
def removeEquipe(request,id):
    Equipe = get_object_or_404(Person,pk=id)
    form = newEquipeForm(request.POST or None,instance = Equipe)

    if request.method ==  'POST':
        Equipe.delete()
        return redirect('lista_equipes')

    return render( request,'confirm_delete.html',{'object':equipe})
