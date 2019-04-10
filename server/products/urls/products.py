from django.urls import path
from products.views import (
    ProductCreate, ProductUpdate, ProductDelete, ProductList, ProductDetail,
    product_rest_list
)


app_name = 'products'

urlpatterns = [
    path('create/', ProductCreate.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='delete'),
    path('<int:pk>/', ProductDetail.as_view(), name='detail'),
    path('', ProductList.as_view(), name='main'),
]

urlpatterns += [
    path('api/', product_rest_list, name='rest_list')
]
