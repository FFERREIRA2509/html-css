from django.urls import include, path
from app_cad_usuarios import views


urlpatterns = [
    path('', views.fazersimulacao, name='fazersimulacao'),
    path('resultadosimulacao/', views.fazersimulacao, name='resultadosimulacao')
]