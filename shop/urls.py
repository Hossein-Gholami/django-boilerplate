from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.detail, name='detail'),
    # add items
    path('add/', views.create_product_item, name='create_product_item'),
    # update
    path('update/<int:product_id>/', views.update_product_item, name='update_product_item'),
    # delete
    path('delete/<int:product_id>/', views.delete_product_item, name='delete_product_item'),
]

