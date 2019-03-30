from django.shortcuts import render
from server.menu import Menu, products


def main(request):
    return render(
        request,
        'main/index.html',
        {
            'title': 'Сундук с сокровищами',
            'link_list': ['main/css/index.css'],
            'products': products,
            'menu': Menu,
        }
    )


def contacts(request):
    return render(
        request,
        'main/contacts.html',
        {
            'title': 'Контакты',
            'link_list': ['main/css/contacts.css'],
            'menu': Menu,
        }
    )
