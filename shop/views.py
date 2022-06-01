from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer
from .forms import ItemForm


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    # template = loader.get_template('shop/index.html')
    # return HttpResponse(template.render(context,request))
    return render(request, 'shop/index.html', context)

def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request,'shop/detail.html', context)


def create_product_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('shop:index')

    return render(request, 'shop/item_form.html', context={'form':form})

def update_product_item(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ItemForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('shop:index')

    return render(request, 'shop/item_form.html', context={'form':form, 'product': product})
    
def delete_product_item(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('shop:index')

    return render(request, 'shop/item_delete.html', context={'product': product})
