from django import template
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    template = loader.get_template('shop/index.html')
    return HttpResponse(template.render(context,request))

