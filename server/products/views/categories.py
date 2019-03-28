from django.shortcuts import render, redirect, get_object_or_404
from products.forms import CategoryModelForm
from products.models import ProductCategory


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
            'link_list': ['categories/css/crut.css'],
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
            'link_list': ['categories/css/crut.css'],
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
            'link_list': ['categories/css/crut.css'],
            'obj': obj,
        }
    )
