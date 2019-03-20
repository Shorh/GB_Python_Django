from django.shortcuts import render
import json


def catalog(request):
    with open('products/fixtures/data/data.json') as file:
        data = json.load(file)
        return render(
            request,
            'products/index.html',
            {
                'title': 'Каталог',
                'link_list': [''],
                'products': data,
                'menu': {itm['name']: 0 for itm in data},
            }
        )


def product_detail(request, pk):
    with open('products/fixtures/data/data.json') as file:
        data = json.load(file)
        return render(
            request,
            'products/detail.html',
            {
                'title': data[pk]['name'],
                'link_list': ['products/css/product.css'],
                'product': data[pk],
                'menu': {itm['name']: 0 for itm in data},
            }
        )
