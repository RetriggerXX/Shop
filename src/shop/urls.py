from django.urls import path
from shop.views import *

urlpatterns = [
    path('hello/', shop_view),
    path('', home_view)
]