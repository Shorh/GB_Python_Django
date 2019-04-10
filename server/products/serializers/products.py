from rest_framework.serializers import ModelSerializer, SerializerMethodField
from products.models import Product


class ProductSerializer(ModelSerializer):
    category = SerializerMethodField()
    is_pure = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'url',
            'name',
            'category',
            'short_description',
            'description',
            'specifications',
            'price_now',
            'price_old',
            'quantity',
            'image',
            'status',
            'is_pure',
            'created',
            'modified',
        ]

    def get_category(self, obj):
        if obj.category:
            return obj.category.name

    def get_is_pure(self, obj):
        return obj.created == obj.modified
