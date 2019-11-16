from django.forms import ModelForm
from django import forms
from .models import *
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker','type':'date'})

class newServoForm(ModelForm): 
    
    class Meta:
        model  = Person
        fields = '__all__'
        widgets = {
            'dt_nasc': DateInput(),
            'obs':     forms.Textarea (attrs={'class':'materialize-textarea','rows':5})       
        }
        


class FormTeste(ModelForm): 
    
    class Meta:
        model  = Person
        fields = '__all__'
        widgets = {
            'dt_nasc': forms.DateInput(attrs ={'class':'datapicker'}),
            'obs':     forms.Textarea (attrs={'class':'materialize-textarea','rows':5})       
        }
        


