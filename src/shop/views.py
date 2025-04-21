from django.shortcuts import render, redirect
from django.http import HttpResponse

from .admin.product import product
from .forms import ModelProductForm
goods = [
    {"good_name": "Плюшевый мишка", "status": "в наличии", "category": "детские"},
    {"good_name": "Конструктор Lego", "status": "нет в наличии", "category": "детские"},
    {"good_name": "Велосипед", "status": "в наличии", "category": "детские"},
    {"good_name": "Пазл", "status": "в наличии", "category": "детские"},
    {"good_name": "Кукольный домик", "status": "нет в наличии", "category": "детские"}
]

users = [
    {"name": "Алиса", "age": 25, "phone": "+79123456789"},
    {"name": "Борис", "age": 30, "phone": "+79219876543"},
    {"name": "Виктор", "age": 22, "phone": "+79331112233"},
    {"name": "Дмитрий", "age": 28, "phone": "+79444555666"},
    {"name": "Елена", "age": 35, "phone": "+79557778899"}
]


# Create your views here.

def info(request):
    return render(request, template_name = "info.html")

def home_view(request):
    return render(request, template_name = 'home.html')

def shop(request):
    return render(request, template_name = 'shop.html')

def clients(request):
    return render(request, template_name = 'clients.html', context = {"users": users})

def children(request):
    children_goods = [good for good in goods if good["category"] == "детские"]
    return render(request, template_name = 'children.html', context = {'goods': children_goods})

def Product_Form(request):

    context = {}


    if request.method == "POST":
        form = ModelProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/shop/add_product")
    context["form"] = ModelProductForm()

    return render(request, template_name='shop.html', context=context)