from django.shortcuts import render
from collections import namedtuple


def main(request):
    Product = namedtuple('Product', 'name url image_url price')
    new = [Product('Каркассон', 'products:karkasson', 'products/img/karkasson.jpg', '1 300')]
    hot = [Product('Мачи Коро', 'products:machi_koro', 'products/img/machi-koro.jpg', '1 000')]
    sale = [Product('Манчкин', 'products:manchkin', 'products/img/manchkin.jpg', '1 000')]

    return render(
        request,
        'main/index.html',
        {
            'title': 'Сундук с сокровищами',
            'link_list': ['main/css/index.css'],
            'new': new,
            'hot': hot,
            'sale': sale,
        }
    )


def contacts(request):
    return render(
        request,
        'main/contacts.html',
        {
            'title': 'Контакты',
            'link_list': ['main/css/contacts.css'],
        }
    )
