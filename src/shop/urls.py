from django.urls import path
from shop.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('info', info, name='info'),
    path('marketplace', shop, name='shop'),
    path('clients', clients, name='clients')
]