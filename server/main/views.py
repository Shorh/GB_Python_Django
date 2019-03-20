from django.shortcuts import render
from products.models import Product


def main(request):
    data = Product.objects.all()
    return render(
        request,
        'main/index.html',
        {
            'title': 'Сундук с сокровищами',
            'link_list': ['main/css/index.css'],
            'products': data,
            'menu': [itm.name for itm in data],
        }
    )


def contacts(request):
    data = Product.objects.all()
    return render(
        request,
        'main/contacts.html',
        {
            'title': 'Контакты',
            'link_list': ['main/css/contacts.css'],
            'menu': [itm.name for itm in data],
        }
    )
