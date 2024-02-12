from django.contrib import admin
from django.urls import path

#from todos.views import home
from todos.views import artigos

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home),
    path('', artigos),
]
