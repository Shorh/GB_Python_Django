from django.urls import path
from products.views import (
    catalog, product_detail, product_create
)


app_name = 'products'

urlpatterns = [
    path('create/', product_create, name='create'),
    path('<int:pk>/', product_detail, name='detail'),
    path('', catalog, name='main'),
]
