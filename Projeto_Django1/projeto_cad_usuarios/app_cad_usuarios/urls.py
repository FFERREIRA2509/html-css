from django.urls import include, path
from app_cad_usuarios import views


urlpatterns = [
    path('formfazersimulacao/', views.fazersimulacao, name='formfazersimulacao'),
    
]