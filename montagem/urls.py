from django.urls import path
from . import views
from . import views_equipe


urlpatterns = [
    path('testelista/',views_equipe.lista_equipes,name ='listaequipesteste'),     
    path('cep/<str:cep>/',views.consultacep,name ='cep'),     
    path('lista/',views.listaServos,name ='lista'),     
    path('novoservo/',views.novoServo,name ='new_servo'),   
    path('novaparoquia/',views.novaParoquia,name ='new_paroquia'),   
    path('novoencontro/',views.novoEncontro,name ='new_encontro'),   
    path('novaequipe/',views_equipe.novaEquipe,name ='new_equipe'),   
    path('delservo/<int:id>/',views.removeServo,name ='del_servo'),   
    path('delparoquia/<int:id>/',views.removeParoquia,name ='del_paroquia'),   
    path('delencontro/<int:id>/',views.removeEncontro,name ='del_encontro'),   
    path('atualizaservo/<int:id>/',views.atualizaServo,name ='upd_servo'),   
    path('atualizaparoquia/<int:id>/',views.atualizaParoquia,name ='upd_paroquia'),   
    path('atualizaEncontro/<int:id>/',views.atualizaEncontro,name ='upd_encontro'),   
    path('servos/',views.listaServos,name ='lista_servos'),   
    path('paroquias/',views.listaParoquias,name ='lista_paroquias'),   
    path('encontros/',views.listaEncontros,name ='lista_encontros'),   
    path('equipes/',views_equipe.lista_equipes,name ='lista_equipes'),   
    path('',views.home,name ='home'),   
   
]