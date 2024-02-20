
from http import server
from django import urls
from django.conf import settings
from django.urls import include, path
from app_cad_usuarios import views
from django.contrib import admin

urlpatterns = [
    # rota, view responsável, nome de referência
    path('',views.home,name='home'),
    path('formfazersimulacao/', views.fazersimulacao, name="fazersimulacao"),
    path("f4contabilidade/", include("f4contabilidade.urls")),
    path("admin/", admin.site.urls),
    
    #path('usuarios/', views.usuarios, name="calculo"),
    #path('resultadosimulacao/', views.usuarios, name="calculo"),
    
]
