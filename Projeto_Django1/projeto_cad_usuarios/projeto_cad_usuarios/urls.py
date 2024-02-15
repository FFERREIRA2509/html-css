
from http import server
from django import urls
from django.conf import settings
from django.urls import include, path
from app_cad_usuarios import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # usuarios.com 
    path('',views.home,name='home'),
    path('usuarios/', views.usuarios, name="listagem_usuarios"),
    path('resultadosimulacao/', views.resultadosimulacao, name="calculo"),
]
