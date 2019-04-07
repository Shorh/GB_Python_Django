from rest_framework.serializers import ModelSerializer
from products.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'category',
            'name',
            'short_description',
            'description',
            'specifications',
            'price_now',
            'price_old',
            'quantity',
            'image',
            'status',
        ]
