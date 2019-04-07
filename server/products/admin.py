from django.contrib import admin
from django.template.loader import render_to_string

from .models import Product, ProductCategory


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'category',
        'name',
        'picture',
        'price_now',
        'price_old',
        'quantity',
        'status',
    ]

    list_filter = [
        'category',
        'name',
        'price_now',
        'price_old',
        'quantity',
        'status',
    ]

    def picture(self, obj):
        return render_to_string(
            'products/components/picture.html',
            {'image': obj.image}
        )


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
