from django.shortcuts import render, redirect
from collections import namedtuple

from .models import Product
from .forms import CategoryModelForm, ProductModelForm


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


def category_create(request):
    form = CategoryModelForm()
    if request.method == 'POST':
        form = CategoryModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:main')

    return render(
        request,
        'categories/create.html',
        {
            'title': 'Создание категории',
            'link_list': ['categories/css/create.css'],
            'form': form,
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
