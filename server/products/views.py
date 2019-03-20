from django.shortcuts import render
from products.models import Product


def catalog(request):
    data = Product.objects.all()
    return render(
        request,
        'products/index.html',
        {
            'title': 'Каталог',
            'link_list': [''],
            'products': data,
            'menu': [itm.name for itm in data],
        }
    )


def product_detail(request, pk):
    data = Product.objects.all()
    return render(
        request,
        'products/detail.html',
        {
            'title': data[pk].name,
            'link_list': ['products/css/product.css'],
            'product': data[pk],
            'menu': [itm.name for itm in data],
        }
    )
