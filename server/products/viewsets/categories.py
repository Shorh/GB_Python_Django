from rest_framework.viewsets import ModelViewSet

from products.models import ProductCategory
from products.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer
