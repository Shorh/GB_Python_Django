from django.urls import path
from products.views import (
    category_create
)


app_name = 'categories'

urlpatterns = [
    path('create/', category_create, name='create'),
]
