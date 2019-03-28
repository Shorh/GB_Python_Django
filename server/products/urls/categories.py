from django.urls import path
from products.views import (
    category_create, category_update, category_delete
)


app_name = 'categories'

urlpatterns = [
    path('create/', category_create, name='create'),
    path('update/<int:pk>/', category_update, name='update'),
    path('delete/<int:pk>/', category_delete, name='delete'),
]
