from django.contrib import admin
from django.urls import path, include

from django.urls import path

from shop_api.views import HomeView, MyDetailView, MyListView, AddProduct, DeleteProduct

urlpatterns = [
    path("my_home/", HomeView.as_view()),  # Главная страница
    path("products/<int:pk>/", MyDetailView.as_view(), name="product_detail"),  # Добавил имя для маршрута product_detail
    path("list/", MyListView.as_view(), name="product_list"),  # Список продуктов
    path('add_product/', AddProduct.as_view()),
    path('delete_product/<int:pk>/', DeleteProduct.as_view(), name='delete_product')


]