from django.urls import include, path
from app_cad_usuarios import views
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.f4, name='f4'),
    path('formfazersimulacao/', views.fazersimulacao, name='fazersimulacao'),
    path('resultadosimulacao/', views.fazersimulacao, name='resultadosimulacao'),
    path('imposto_de_renda/', views.imposto_de_renda, name='imposto_de_renda'),
    path('artigos/', views.artigos, name='artigos'),
    path('serviços/', views.serviços, name='serviços'),
    path('modelo/', views.modelo, name='modelo'),
    ]