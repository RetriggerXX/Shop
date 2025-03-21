from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def shop_view(request):
    return HttpResponse("<h1>Hello Django<h1>")

def home_view(request):
    return HttpResponse("<h1>Home page<h1>")