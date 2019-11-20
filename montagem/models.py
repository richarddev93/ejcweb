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
    nome = models.CharField(verbose_name = 'Nome', max_length=50)
    sobrenome=models.CharField(max_length=70)
    apelido=models.CharField(max_length=20,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    tel1=models.CharField(blank=True,null=True,max_length=13)
    tel2=models.CharField(blank=True,null=True,max_length=13)
    foto=models.ImageField(upload_to='profile_picture',blank=True,null=True)
    dt_nasc=models.DateField(blank=True,null=True)
    nivel=models.CharField(blank=True,choices=escolhas_nivel,max_length=30,verbose_name='Nível:')
    ##Endereco##
    cep=models.IntegerField()
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
       return self.tema##verificarcomoatribuironome+ano
    def __str__(self):
        return self.get_name_encontro()
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
        (u'canto','canto'),
        (u'compras',u'Compras'),
        (u'cozinha',u'Cozinha'),
        (u'circulo',u'Círculo'),
        (u'co_gerais',u'Coord.Gerais'),
        (u'dirigentes',u'Dirigentes'),
        (u'espirit',u'Espiritualizador'),
        (u'interc',u'Intercessão'),
        (u'lanche',u'Lanche'),
        (u'faxina',u'FaxinaeLimpeza'),
        (u'sala',u'Sala'),
        (u'secretaria',u'Secretaria'),
        (u'transito',u'OrdemeTrânsito'),
        (u'visitação',u'Visitação'),
        )

    escolhas_status=((u'c','Enviado'),(u'r','Recusado'),(u'd','Desistiu'),(u'a','Aceito'),(u's','SemRetornoouContato'),)
    status_conv=models.CharField(choices=escolhas_status,max_length=30,verbose_name='Status:')
    nome_equipe=models.CharField(choices=escolhas_equipe,max_length=30,verbose_name='Equipes:')
    obs = models.CharField(max_length=60,blank=True,null=True)
    servos = models.OneToOneField(Person,on_delete=models.PROTECT,null=True)
    encontros = models.ForeignKey(Encontro,on_delete=models.PROTECT,null=True)
    def __str__(self):
        return self.nome_equipe