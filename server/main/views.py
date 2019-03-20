from django.shortcuts import render
import json


def main(request):
    with open('products/fixtures/data/data.json') as file:
        return render(
            request,
            'main/index.html',
            {
                'title': 'Сундук с сокровищами',
                'link_list': ['main/css/index.css'],
                'products': json.load(file),
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
