from django.urls import path
from products.views import (
    product_list, product_detail, product_create, product_update,
    product_delete, product_rest_list
)


app_name = 'products'

urlpatterns = [
    path('create/', product_create, name='create'),
    path('update/<int:pk>/', product_update, name='update'),
    path('delete/<int:pk>/', product_delete, name='delete'),
    path('<int:pk>/', product_detail, name='detail'),
    path('', product_list, name='main'),
]

urlpatterns += [
    path('api/', product_rest_list, name='rest_list')
]
