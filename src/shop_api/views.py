from django.core.serializers import serialize
from django.http.response import HttpResponse, JsonResponse
from django.template.context_processors import request
from rest_framework.response import Response
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from shop.models import Product, Order
from shop_api.serializers import ShopSerializer, OrderSerializer

# class HomeView(TemplateView):
#     template_name = "home.html"
#
#
# class MyDetailView(DetailView):
#     model = Product
#     template_name = 'product_detail.html'
#
#     def get_queryset(self):
#         return Product.objects.all()
#
# class MyListView(ListView):
#     model = Product
#     template_name = 'product_list.html'
#     paginate_by = 1
#     context_object_name = 'product_list'
#
#     def get_queryset(self):
#         return Product.objects.all()
#
#
#
#
# from rest_framework import mixins
# from rest_framework import generics
#
# class AddProduct(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ShopSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class DeleteProduct(mixins.ListModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ShopSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#
#         product = self.get_object()
#         self.perform_destroy(product)
#
#         return redirect("/api/add_product/")


class GetProduct(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ShopSerializer(product, many = True)
        return Response(serializer.data)

class PostProduct(APIView):
    def post(self, request):
        serializer = ShopSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PutProduct(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ShopSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ShopSerializer(product, data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeleteProduct(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ShopSerializer(product)
        return Response(serializer.data)

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response()


class GetOrder(APIView):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
