from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from rest_framework.parsers import JSONParser
from shop.models import Product
from shop_api.serializers import ShopSerializer

class HomeView(TemplateView):
    template_name = "home.html"


class MyDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_queryset(self):
        return Product.objects.all()

class MyListView(ListView):
    model = Product
    template_name = 'product_list.html'
    paginate_by = 1
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all()




from rest_framework import mixins
from rest_framework import generics

class AddProduct(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ShopSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DeleteProduct(mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ShopSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):

        product = self.get_object()
        self.perform_destroy(product)

        return redirect("/api/add_product/")
