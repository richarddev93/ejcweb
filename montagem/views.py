from django.shortcuts import render,redirect,get_object_or_404
from django.core import paginator
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http.response import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Person,Paroquia,Encontro,Membros,Equipe
from django.contrib.auth.decorators import login_required
from .forms import newServoForm,newParoquiaForm,newEncontroForm
from django.http import HttpRequest
from datetime import datetime,date



import requests,sys


@login_required
def home(request):
    return render(request,'home.html')

@login_required    
def listaServos(request):
    serial = False    
    filter_equipe = request.GET.get("filtra_Equipe",'')
    query = request.GET.get("busca",'')
    sort = request.GET.get("ordenar", '')
    page = request.GET.get("page", '')
    params = [serial,query,sort,filter_equipe]
    
    try:
        servos = consultaBanco(params)
        servos = Paginator(servos,20)#definindo a paginação
        servos = servos.page(page)
    except  PageNotAnInteger :
        servos = servos.page(1)
    except EmptyPage :
        servos = paginator.page(paginator.num_page)

    if request.method == 'GET':  

        return render(request,'lista_servos.html',{'servos':servos,'quant':len(servos)})

    elif request.method == 'POST':
        return HttpResponse ("Logo faz algo")

 
def consultaBanco(params):
    if params[0] == True:
         
         data = serializers.serialize("json", Person.objects.all())
    elif params[1]:
         data = Person.objects.filter(nome__icontains = params[1])
    elif params[2]:
         data = Person.objects.all().order_by(params[2])     
    elif params[3]:
        
        data1 = Membros.objects.select_related("person").all().filter(equipe__nome_equipe__icontains=params[3]).values("person_id")
                
        ids=[id['person_id'] for id in data1] #pegando os ids dos servos que pertencem a query acima
         
        if len(data1)>=1:
            data = Person.objects.filter(id__in=ids)
        else:
            data = Person.objects.all()#Por enquanto retornando todos novamente até tratar o retorno zero
        
    else:
         data = Person.objects.all()
    return data

@login_required
def novoServo(request):
    form = newServoForm(request.POST or None, request.FILES or None)
     
    if form.is_valid():
        post = form.save(commit=False)
        data = date.today()
        diff = ((data - post.dt_nasc)/365).days  
        post.idade = diff
        form.save()
        return redirect('lista_servos')
    
    return render (request,'form_servo.html',{'form': form})


@login_required
def atualizaServo(request,id):
    servo = get_object_or_404(Person,pk=id)
    testeObj = servo
    form = newServoForm(request.POST or None,request.FILES or None ,instance = servo )
    if form.is_valid():
        post = form.save(commit=False)
        data = date.today()
        diff = ((data - post.dt_nasc)/365).days  
        post.idade = diff

        form.save()
        return redirect('lista_servos')

    return render (request,'form_servo.html',{'form': form})


@login_required    
def removeServo(request,id):
    servo = get_object_or_404(Person,pk=id)
    form = newServoForm(request.POST or None,instance =servo)

    if request.method ==  'POST':
        servo.delete()
        return redirect('lista_servos')

    return render( request,'confirm_delete.html',{'object':servo})

##Defs da Paróquia
@login_required
def listaParoquias(request):
    serial = False    
    query = request.GET.get("busca",'')
    sort = request.GET.get("ordenar", '')
    page = request.GET.get("page", '')
    params = [serial,query,sort]#passando para o metode busca todos os params necessarios

    try:
        paroquias = consultaBanco1(params)
        paroquias = Paginator(paroquias,25)#definindo a paginação
        paroquias = paroquias.page(page)#passando apenas os itens que queo na pagina para o paroquias
    except  PageNotAnInteger :
        paroquias = paroquias.page(1)
    except EmptyPage :
        paroquias = paginator.page(paginator.num_page)
    
    form = newParoquiaForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request,'paroquia.html',{'paroquias':paroquias,'form': form })


def consultaBanco1(params):
    if params[0] == True:
         data = serializers.serialize("json", Paroquia.objects.all())
    elif params[1]:
         data = Paroquia.objects.filter(nome_paroquia__icontains = params[1])
    elif params[2]:
         data = Paroquia.objects.all().order_by(params[2])     
    else:
         data = Paroquia.objects.all()
    return data

@login_required
def novaParoquia(request):
    form = newParoquiaForm(request.POST or None)
    # context = {
    #     'form':form
    # }
    # html_form = render_to_string('formpar.html',context,request=request)
    # return JsonResponse({'html_form':html_form})

    if form.is_valid():
        form.save()
        return redirect('lista_paroquias')
    
    return render (request,'formpar.html',{'form': form})
    #return HttpResponse(form)

@login_required
def atualizaParoquia(request,id):
    paroquia = get_object_or_404(Paroquia,pk=id)
    form = newParoquiaForm(request.POST or None,instance = paroquia )
    
    if form.is_valid():
        form.save()
        return redirect('lista_paroquias')

    return render (request,'paroquia.html',{'form': form})

@login_required    
def removeParoquia(request,id):
    paroquia = get_object_or_404(Paroquia,pk=id)
    form = newServoForm(request.POST or None,instance =paroquia)

    if request.method ==  'POST':
        paroquia.delete()
        return redirect('lista_paroquias')

    return render( request,'confirm_delete.html',{'object':paroquia})

##Defs da Encontro
@login_required
def listaEncontros(request):
    serial = False    
    query = request.GET.get("busca",'')
    sort = request.GET.get("ordenar", '')
    page = request.GET.get("page", '')
    params = [serial,query,sort]#passando para o metode busca todos os params necessarios

    try:
        encontros = consultaBanco2(params)
        encontros = Paginator(encontros,25)#definindo a paginação
        encontros = encontros.page(page)#passando apenas os itens que queo na pagina para o paroquias
    except  PageNotAnInteger :
        encontros = encontros.page(1)
    except EmptyPage :
        encontros = paginator.page(paginator.num_page)

    return render(request,'lista_encontros.html',{'encontros':encontros })


def consultaBanco2(params):
    if params[0] == True:
         data = serializers.serialize("json", Encontro.objects.all())
    elif params[1]:
         data = Encontro.objects.filter(ano__icontains = params[1])
    elif params[2]:
         data = Encontro.objects.all().order_by(params[2])     
    else:
         data = Encontro.objects.all()
    return data

@login_required
def novoEncontro(request):
    form = newEncontroForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect('lista_encontros')

    return render (request,'form_encontro.html',{'form': form})

@login_required
def atualizaEncontro(request,id):
    encontro = get_object_or_404(Encontro,pk=id)
    form = newEncontroForm(request.POST or None,request.FILES or none ,instance = encontro )
    if form.is_valid():
        form.save()
        return redirect('lista_encontros')

    return render (request,'form_encontro.html',{'form': form})

@login_required    
def removeEncontro(request,id):
    encontro = get_object_or_404(Encontro,pk=id)
    form = newServoForm(request.POST or None,instance =encontro)

    if request.method ==  'POST':
        paroquia.delete()
        return redirect('lista_encontros')

    return render( request,'confirm_delete.html',{'object':encontro})




def consultacep(request,cep):
    if request.method =='GET':
        url = 'https://viacep.com.br/ws/'+cep+'/json/' 
        # params = {'year': year, 'author': author}
        # r = requests.get(url, params=params)
        r = requests.get(url)
        # r = render_to_string(r)
        # books_list = {'books':books['results']}
    return render( request,'form_servo.html',{'rua':r['logradouro']})
