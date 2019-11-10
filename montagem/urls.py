from django.urls import path
from . import views


urlpatterns = [
    path('lista/',views.listaServos,name ='lista'),   
    path('novoservo/',views.novoServo,name ='new_servo'),   
    path('delservo/<int:id>/',views.removeServo,name ='del_servo'),   
    path('atualizaservo/<int:id>/',views.atualizaServo,name ='upd_servo'),   
    path('servos/',views.listaServos,name ='lista_servos'),   
    path('',views.home,name ='home'),   
   
]