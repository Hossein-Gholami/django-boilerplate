from django import forms
from .models import Product


class ItemForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'desc', 'price', 'image')

