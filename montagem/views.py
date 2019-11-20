from django.shortcuts import render,redirect,get_object_or_404
from django.core import paginator
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http.response import HttpResponse
from django.core import serializers
from .models import Person
from .forms import newServoForm


def home(request):
    return render(request,'home.html')
    
def listaServos(request):
    serial = False    
    query = request.GET.get("busca",'')
    sort = request.GET.get("ordenar", '')
    page = request.GET.get("page", '')
    params = [serial,query,sort]

        
    try:
        servos = consultaBanco(params)
        servos = Paginator(servos,25)
        servos = servos.page(page)
    except  PageNotAnInteger :
        servos = servos.page(1)
    except EmptyPage :
        servos = paginator.page(paginator.num_page)


    if request.method == 'GET':        
        return render(request,'lista_servos.html',{'servos':servos})

    elif request.method == 'POST':
        return HttpResponse ("Logo faz algo")
    

def consultaBanco(params):
    if params[0] == True:
         data = serializers.serialize("json", Person.objects.all())
    elif params[1]:
         data = Person.objects.filter(nome__icontains = params[1])
    elif params[2]:
         data = Person.objects.all().order_by(params[2])     
    else:
         data = Person.objects.all()
    return data

def novoServo(request):
    form = newServoForm(request.POST or None, request.FILES or None)
    # form = FormTeste(request.POST or None, request.FILES or None)
   
    if form.is_valid():
        form.save()
        return redirect('lista_servos')
    
    # return render (request,'formTeste.html',{'form': form})
    return render (request,'form_servo.html',{'form': form})
    #return HttpResponse(form)

def atualizaServo(request,id):
    servo = get_object_or_404(Person,pk=id)
    testeObj = servo
    form = newServoForm(request.POST or None,instance = servo )
    # form = FormTeste(request.POST or None, request.FILES or None,instance = servo )
    if form.is_valid():
        form.save()
        return redirect('lista_servos')

    return render (request,'form_servo.html',{'form': form})
    # return render (request,'formTeste.html',{'form': form})
    
    
    
def removeServo(request,id):
    servo = get_object_or_404(Person,pk=id)
    form = newServoForm(request.POST or None,instance =servo)

    if request.method ==  'POST':
        servo.delete()
        return redirect('lista_servos')

    return render( request,'confirm_delete.html',{'object':servo})


