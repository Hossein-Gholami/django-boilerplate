from django import template
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    template = loader.get_template('shop/index.html')
    return HttpResponse(template.render(context,request))

