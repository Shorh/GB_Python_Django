from django.shortcuts import render
import json


def catalog(request):
    with open('products/fixtures/data/data.json') as file:
        return render(
            request,
            'products/index.html',
            {
                'title': 'Каталог',
                'link_list': [''],
                'products': json.load(file),
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
