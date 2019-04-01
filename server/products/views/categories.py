from django.shortcuts import render, redirect, get_object_or_404
from products.models import ProductCategory

from products.models import ProductCategory
from products.forms import CategoryModelForm


def category_list(request):
    return render(
        request,
        'categories/index.html',
        {
            'title': 'Категории',
            'link_list': [''],
            'categories': ProductCategory.objects.all(),
            'menu': ProductCategory.objects.all(),
        }
    )


def category_detail(request, pk):
    obj = get_object_or_404(ProductCategory, pk=pk)
    return render(
        request,
        'categories/detail.html',
        {
            'title': obj.name,
            'link_list': ['products/css/product.css'],
            'category': obj,
            'menu': ProductCategory.objects.all(),
        }
    )


def category_create(request):
    form = CategoryModelForm()
    if request.method == 'POST':
        form = CategoryModelForm(
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
            'title': 'Создание категории',
            'link_list': ['server/css/crud.css'],
            'menu': ProductCategory.objects.all(),
            'form': form,
        }
    )


def category_update(request, pk):
    obj = get_object_or_404(ProductCategory, pk=pk)
    form = CategoryModelForm(
        instance=obj
    )

    if request.method == 'POST':
        form = CategoryModelForm(
            data=request.POST,
            files=request.FILES,
            instance=obj
        )

        if form.is_valid():
            form.save()
            return redirect('products:main')

    return render(
        request,
        'categories/update.html',
        {
            'title': 'Изменение категории',
            'link_list': ['server/css/crud.css'],
            'menu': ProductCategory.objects.all(),
            'form': form,
            'obj': obj,
        }
    )


def category_delete(request, pk):
    obj = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('products:main')

    return render(
        request,
        'categories/delete.html',
        {
            'title': 'Удаление категории',
            'link_list': ['server/css/crud.css'],
            'menu': ProductCategory.objects.all(),
            'obj': obj,
        }
    )
