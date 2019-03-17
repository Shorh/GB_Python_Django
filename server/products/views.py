from django.shortcuts import render
from collections import namedtuple


def catalog(request):
    Product = namedtuple('Product', 'name url image_url price')
    products = [
        Product('Каркассон', 'karkasson', '/static/products/img/karkasson.jpg', '1 300'),
        Product('Мачи Коро', 'machi_koro', '/static/products/img/machi-koro.jpg', '1 000'),
        Product('Манчкин', 'manchkin', '/static/products/img/manchkin.jpg', '1 000'),
    ]

    return render(
        request,
        'products/index.html',
        {
            'title': 'Каталог',
            'link_list': [''],
            'products': products,
        }
    )


def karkasson(request):
    return render(
        request,
        'products/karkasson.html',
        {
            'title': 'Каркассон',
            'link_list': ['products/css/product.css'],
        }
    )


def machi_koro(request):
    return render(
        request,
        'products/machi-koro.html',
        {
            'title': 'Мачи Коро',
            'link_list': ['products/css/product.css'],
        }
    )


def manchkin(request):
    return render(
        request,
        'products/manchkin.html',
        {
            'title': 'Манчкин',
            'link_list': ['products/css/product.css'],
        }
    )
