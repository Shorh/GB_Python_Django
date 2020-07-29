from rest_framework.serializers import ModelSerializer, SerializerMethodField
from products.models import ProductCategory


class CategorySerializer(ModelSerializer):
    is_pure = SerializerMethodField()

    class Meta:
        model = ProductCategory
        fields = [
            'url',
            'name',
            'description',
            'is_pure',
            'created',
            'modified',
        ]

    def get_is_pure(self, obj):
        return obj.created == obj.modified
