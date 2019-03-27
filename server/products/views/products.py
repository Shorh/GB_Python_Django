from django.shortcuts import render, redirect
from collections import namedtuple

from products.models import Product
from products.forms import ProductModelForm


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


def product_create(request):
    form = ProductModelForm()
    if request.method == 'POST':
        form = ProductModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:main')

    return render(
        request,
        'categories/create.html',
        {
            'title': 'Создание продукта',
            'link_list': ['products/css/create.css'],
            'form': form,
        }
    )
