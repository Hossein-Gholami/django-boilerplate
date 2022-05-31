from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'price')

# Register your models here.

admin.site.register(Product, ProductAdmin)
