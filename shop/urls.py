from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.detail, name='detail'),
    # add items
    path('add/', views.create_product_item, name='create_product_item'),
]

