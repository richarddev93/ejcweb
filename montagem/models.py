from django.db import models

# Servos.

class Person(models.Model):
    escolhas_nivel = (
        (u'dir_espiritual',u'Diretor Espiritual'),
        (u'coord',u'Coordenador Geral'),
        (u'coord_equipe',u'Coordenador de Equipe'),
        (u'dirigente',u'Dirigente'),
        (u'servo',u'Servo'),
        (u'convidado',u'Convidado'),
        (u'encontrista',u'Encontrista'),
    )
    escolhas_estado_civil = (
        (u'casado',u'Casado'),
        (u'solteiro',u'Solteiro')
     )
    nome = models.CharField(verbose_name = 'Nome', max_length=50)
    sobrenome=models.CharField(max_length=70)
    apelido=models.CharField(max_length=20,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    tel1=models.CharField(blank=True,null=True,max_length=15)
    tel2=models.CharField(blank=True,null=True,max_length=15)
    foto=models.ImageField(upload_to='profile_picture',blank=True,null=True)
    dt_nasc=models.DateField(blank=True,null=True)
    nivel=models.CharField(blank=True,choices=escolhas_nivel,max_length=30,verbose_name='Nível:')
    ##Endereco##
    cep=models.CharField(max_length=8)
    logradouro=models.CharField(max_length=60)
    numero=models.IntegerField()
    complemento=models.CharField(max_length=40)
    bairro=models.CharField(max_length=40)
    localidade=models.CharField(max_length=60)
    uf=models.CharField(max_length=2)
    paroquia=models.ForeignKey('paroquia',on_delete=models.PROTECT,blank=True,null=True)
    #controle#
    dtcriacao = models.DateField(auto_now_add=True,blank=False,null=False)
    status  = models.BooleanField(default=True,editable=False)
    obs = models.TextField(blank=True,null =True,max_length=200)
    idade = models.IntegerField(default=0,editable=False)
    estado_civil =  models.CharField(max_length=8,choices=escolhas_estado_civil,blank=True,null=True)

    def get_fullname(self):
        if self.apelido!='':
            return self.apelido
        else:
            return self.nome+""+self.sobrenome
    def __str__(self):
        return  self.nome
    class Meta:
        verbose_name = ("Servo")
        verbose_name_plural = ("Servos")

#Encontro
class Encontro(models.Model):

    ano     = models.IntegerField()
    tema    = models.CharField(max_length=30,blank=True,null=True)
    local   = models.CharField(max_length=30,blank=True,null=True)
    dt_ini  = models.DateField(blank=True,null=True)
    dt_fim  = models.DateField(blank=True,null=True)
    desc    = models.CharField(max_length=70,blank=True,null=True)
    cep=models.IntegerField(blank=True,null=True)
    logradouro=models.CharField(max_length=60,blank=True,null=True)
    numero=models.IntegerField(blank=True,null=True)
    complemento=models.CharField(max_length=40,blank=True,null=True)
    bairro=models.CharField(max_length=40,blank=True,null=True)
    localidade=models.CharField(max_length=60,blank=True,null=True)
    uf=models.CharField(max_length=2,blank=True,null=True)

    def get_name_encontro(self):
       return self.ano##verificarcomoatribuironome+ano
    def __str__(self):
        return str(self.get_name_encontro())
#Paroquias
class Paroquia(models.Model):
    nome_paroquia=models.CharField(max_length=30)
    regiao=models.CharField(max_length=30,blank=True,null=True)

    def __str__(self):
        return self.nome_paroquia


#Equipes
class Equipe(models.Model):

    escolhas_equipe=(
        (u'animacao','Animação'),
        (u'espera','Espera'),
        (u'canto','Canto'),
        (u'compras',u'Compras'),
        (u'cozinha',u'Cozinha'),
        (u'circulo',u'Círculo'),
        (u'co_gerais',u'Coord.Gerais'),
        (u'dirigentes',u'Dirigentes'),
        (u'espirit',u'Espiritualizador'),
        (u'interc',u'Intercessão'),
        (u'lanche',u'Lanche'),
        (u'faxina',u'Faxina e Limpeza'),
        (u'sala',u'Sala'),
        (u'secretaria',u'Secretaria'),
        (u'transito',u'Ordem e Trânsito'),
        (u'visitação',u'Visitação'),
        )

    nome_equipe=models.CharField(choices=escolhas_equipe,max_length=30,verbose_name='Equipes:')
    ano = models.IntegerField()
    obs = models.CharField(max_length=60,blank=True,null=True)
    # membs = models.ForeignKey(Person,on_delete=models.PROTECT)
    encontro = models.ForeignKey(Encontro,on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_equipe 


class Membros(models.Model):
    opcoes_status=((u'ac','Aguardando Convite'),(u'e','Convite Enviado'),(u'r','Convite Recusado'),(u'd','Desistiu'),(u'a','Aceito'),(u's','Sem Retorno'),)

    # person = models.ForeignKey(Person, on_delete=models.PROTECT)
    person = models.OneToOneField(Person, on_delete=models.PROTECT,related_name='person')
    equipe = models.ForeignKey(Equipe,on_delete=models.PROTECT,related_name='equipe')
    #equipe = models.OneToOneField(Equipe,on_delete=models.PROTECT)
    dt_convite = models.DateField()
    status_conv=models.CharField(choices=opcoes_status,max_length=1,verbose_name='Status:',default='Aguardando Convite')

    def __str__(self):
        return self.person.nome