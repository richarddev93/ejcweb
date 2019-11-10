from django.forms import ModelForm,forms
from .models import *

escolhas_nivel = [
        (u'dir_espiritual',u'DiretorEspiritual'),
        (u'coord',u'CoordenadorGeral'),
        (u'coord_equipe',u'CoordenadordeEquipe'),
        (u'dirigente',u'Dirigente'),
        (u'servo',u'Servo'),
        (u'convidado',u'Convidado'),
        ]

class newServoForm(ModelForm): 
    
    class Meta:
        model  = Person
        #fields = ['nome','sobrenome','apelido','email','foto',
        #'dt_nasc','nivel','encontrista',
        #'cep','logradouro','numero','complemento','bairro','localidade','uf',
        #'paroquia']
        fields = '__all__'
        widgets = choices=escolhas_nivel
