from django.shortcuts import render
from django.http import HttpResponse

#testando apenas

def home(request):
    return render(request, "todos/home.html")



