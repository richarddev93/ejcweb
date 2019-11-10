from django.shortcuts import render,redirect,get_object_or_404
from django.http.response import HttpResponse
from django.core import serializers
from .models import Person
from .forms import newServoForm

def home(request):
    return render(request,'home.html')
    
def listaServos(request):
    serial = False    
    query = request.GET.get("busca",'')
    servos = consultaBanco(serial,query)
    sizeList = len(servos)

    if request.method == 'GET':
        
        return render(request,'lista_servos.html',{'servos':servos})

    elif request.method == 'POST':
        return HttpResponse ("Logo faz algo")
    

def consultaBanco(serial,query):
    if serial == True:
         data = serializers.serialize("json", Person.objects.all())
    elif query:
         data = Person.objects.filter(nome__icontains = query)
    else:
         data = Person.objects.all()
    return data

def novoServo(request):
    form = newServoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_servos')

    return render (request,'form_servo.html',{'form': form})

def atualizaServo(request,id):
    servo = get_object_or_404(Person,pk=id)
    form = newServoForm(request.POST or None,instance = servo )
    if form.is_valid():
        form.save()
        return redirect('lista_servos')

    return render (request,'form_servo.html',{'form': form})
    
def removeServo(request,id):
    servo = get_object_or_404(Person,pk=id)
    form = newServoForm(request.POST or None,instance =servo)

    if request.method ==  'POST':
        servo.delete()
        return redirect('lista_servos')

    return render( request,'confirm_delete.html',{'object':servo})


