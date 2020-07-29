from django.urls import path
from products.views import (
    CategoryCreate, CategoryUpdate, CategoryDelete, CategoryList, CategoryDetail
)


app_name = 'categories'

urlpatterns = [
    path('create/', CategoryCreate.as_view(), name='create'),
    path('update/<int:pk>/', CategoryUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', CategoryDelete.as_view(), name='delete'),
    path('<int:pk>/', CategoryDetail.as_view(), name='detail'),
    path('', CategoryList.as_view(), name='main'),
]
