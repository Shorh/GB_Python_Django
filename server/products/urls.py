from django.urls import path
from .views import (
    catalog, product_detail
)


app_name = 'products'

urlpatterns = [
    path('<int:pk>/', product_detail, name='detail'),
    path('', catalog, name='main'),
]
