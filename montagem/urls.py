from django.urls import path
from . import views


urlpatterns = [
    path('lista/',views.listaServos,name ='lista'),     
    path('novoservo/',views.novoServo,name ='new_servo'),   
    path('novaparoquia/',views.novaParoquia,name ='new_paroquia'),   
    path('novoencontro/',views.novoEncontro,name ='new_encontro'),   
    path('delservo/<int:id>/',views.removeServo,name ='del_servo'),   
    path('delparoquia/<int:id>/',views.removeParoquia,name ='del_paroquia'),   
    path('delencontro/<int:id>/',views.removeEncontro,name ='del_encontro'),   
    path('atualizaservo/<int:id>/',views.atualizaServo,name ='upd_servo'),   
    path('atualizaparoquia/<int:id>/',views.atualizaParoquia,name ='upd_paroquia'),   
    path('atualizaEncontro/<int:id>/',views.atualizaEncontro,name ='upd_encontro'),   
    path('servos/',views.listaServos,name ='lista_servos'),   
    path('paroquias/',views.listaParoquias,name ='lista_paroquias'),   
    path('encontros/',views.listaEncontros,name ='lista_encontros'),   
    path('',views.home,name ='home'),   
   
]