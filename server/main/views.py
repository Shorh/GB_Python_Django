from django.shortcuts import render
from products.models import Product
from collections import namedtuple


def main(request):
    data = Product.objects.all()
    Menu = namedtuple('Menu', 'name, id')
    return render(
        request,
        'main/index.html',
        {
            'title': 'Сундук с сокровищами',
            'link_list': ['main/css/index.css'],
            'products': data,
            'menu': [Menu(itm.name, itm.id) for itm in data],
        }
    )


def contacts(request):
    data = Product.objects.all()
    Menu = namedtuple('Menu', 'name, id')
    return render(
        request,
        'main/contacts.html',
        {
            'title': 'Контакты',
            'link_list': ['main/css/contacts.css'],
            'menu': [Menu(itm.name, itm.id) for itm in data],
        }
    )
