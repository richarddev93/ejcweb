from django.forms import ModelForm
from django import forms
from .models import *
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker','type':'date'})
nome = Person.objects.values('nome')
class newServoForm(ModelForm): 
    
    class Meta:
        model  = Person
        fields = '__all__'
        widgets = {
            'tel1': forms.TextInput(attrs={'data-mask':'(00) 00000-0000'}),
            'tel2': forms.TextInput(attrs={'data-mask':'(00) 00000-0000'}),
            'dt_nasc': forms.DateInput(attrs ={'class':'datepicker'}),
            'obs':     forms.Textarea (attrs={'class':'materialize-textarea','rows':5})  ,
        }

class newParoquiaForm(ModelForm): 
    
    class Meta:
        model  = Paroquia
        fields = '__all__'
       
class newEncontroForm(ModelForm): 
    
    class Meta:
        model  = Encontro
        fields = '__all__'



