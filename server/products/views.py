from django.shortcuts import render
from products.models import Product
from collections import namedtuple


def catalog(request):
    data = Product.objects.all()
    Menu = namedtuple('Menu', 'name, id')
    return render(
        request,
        'products/index.html',
        {
            'title': 'Каталог',
            'link_list': [''],
            'products': data,
            'menu': [Menu(itm.name, itm.id) for itm in data],
        }
    )


def product_detail(request, pk):
    data = Product.objects.all()
    Menu = namedtuple('Menu', 'name, id')
    return render(
        request,
        'products/detail.html',
        {
            'title': data.get(id=pk).name,
            'link_list': ['products/css/product.css'],
            'product': data.get(id=pk),
            'menu': [Menu(itm.name, itm.id) for itm in data],
        }
    )
