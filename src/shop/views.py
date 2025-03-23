from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def info(request):
    return render(request, template_name="info.html")

def home_view(request):
    return render(request, template_name='home.html')

def shop(request):
    return render(request, template_name='shop.html')

def clients(request):
    return render(request, template_name='clients.html')