from django.shortcuts import render, redirect, get_object_or_404
from server.menu import Menu, products

from products.models import Product
from products.forms import ProductModelForm


def product_list(request):
    return render(
        request,
        'products/index.html',
        {
            'title': 'Каталог',
            'link_list': [''],
            'products': products,
            'menu': Menu,
        }
    )


def product_detail(request, pk):
    return render(
        request,
        'products/detail.html',
        {
            'title': products.get(id=pk).name,
            'link_list': ['products/css/product.css'],
            'product': products.get(id=pk),
            'menu': Menu,
        }
    )


def product_create(request):
    form = ProductModelForm()
    if request.method == 'POST':
        form = ProductModelForm(
            data=request.POST,
            files=request.FILES,
        )
        if form.is_valid():
            form.save()
            return redirect('products:main')

    return render(
        request,
        'categories/create.html',
        {
            'title': 'Создание продукта',
            'link_list': ['products/css/crud.css'],
            'menu': Menu,
            'form': form,
        }
    )


def product_update(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    form = ProductModelForm(
        instance=obj
    )

    if request.method == 'POST':
        form = ProductModelForm(
            data=request.POST,
            files=request.FILES,
            instance=obj,
        )

        if form.is_valid():
            form.save()
            return redirect('products:main')

    return render(
        request,
        'products/update.html',
        {
            'title': 'Изменение продукта',
            'link_list': ['products/css/crud.css'],
            'menu': Menu,
            'form': form,
            'obj': obj,
        }
    )


def product_delete(request, pk):
    obj = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('products:main')

    return render(
        request,
        'products/delete.html',
        {
            'title': 'Удаление продукта',
            'link_list': ['products/css/crud.css'],
            'menu': Menu,
            'obj': obj,
        }
    )
