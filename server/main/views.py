from django.shortcuts import render
import json


def main(request):
    with open('products/fixtures/data/data.json') as file:
        data = json.load(file)
        return render(
            request,
            'main/index.html',
            {
                'title': 'Сундук с сокровищами',
                'link_list': ['main/css/index.css'],
                'products': data,
                'menu': [itm['name'] for itm in data],
            }
        )


def contacts(request):
    with open('products/fixtures/data/data.json') as file:
        data = json.load(file)
        return render(
            request,
            'main/contacts.html',
            {
                'title': 'Контакты',
                'link_list': ['main/css/contacts.css'],
                'menu': [itm['name'] for itm in data],
            }
        )
