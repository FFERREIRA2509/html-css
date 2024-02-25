from django.urls import include, path
from app_cad_usuarios import views


urlpatterns = [
    path('', views.fazersimulacao, name='fazersimulacao'),
    path('processa_formulario/', views.processa_formulario, name='processa_formulario')
]