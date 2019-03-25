from django.urls import path
from .views import (
    catalog, product_detail, category_create, product_create
)


app_name = 'products'

urlpatterns = [
    path('category_create/', category_create, name='category_create'),
    path('product_create/', product_create, name='product_create'),
    path('<int:pk>/', product_detail, name='detail'),
    path('', catalog, name='main'),
]
