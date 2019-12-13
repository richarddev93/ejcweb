from django.shortcuts import render,redirect,get_object_or_404
from django.core import paginator
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http.response import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Equipe,Membros

from .forms import newServoForm,newParoquiaForm,newEncontroForm

def listaEquipes(request):
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

    elif request.method == 'POST':
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
