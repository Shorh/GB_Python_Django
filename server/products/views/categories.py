from django.shortcuts import render, redirect
from products.forms import CategoryModelForm


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
