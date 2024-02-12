from django.shortcuts import render
from django.http import HttpResponse


def artigos(request):
    return render(request, "todos/artigos.html")


#def home(request):
 #   return render(request, "todos/home.html") 


