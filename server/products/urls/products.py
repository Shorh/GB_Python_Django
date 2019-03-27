from django.urls import path
from products.views import (
    catalog, product_detail, product_create, product_update, product_delete
)


app_name = 'products'

urlpatterns = [
    path('create/', product_create, name='create'),
    path('update/<int:pk>/', product_update, name='update'),
    path('delete/<int:pk>/', product_delete, name='delete'),
    path('<int:pk>/', product_detail, name='detail'),
    path('', catalog, name='main'),
]
