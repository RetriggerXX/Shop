from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('info', info, name='info'),
    path('marketplace', shop, name='shop'),
    path('clients', clients, name='clients'),
    path('marketplace/children', children, name='children'),
    path('add_product', Product_Form, name="ProductForm" )
]