from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.http import JsonResponse
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView
)
from django.urls import reverse_lazy

from products.models import Product, ProductCategory
from products.forms import ProductModelForm


class ProductList(ListView):
    model = Product
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог'
        context['link_list'] = ['']
        context['menu'] = ProductCategory.objects.all()
        context['products'] = Product.objects.all()[:3]

        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_object().name
        context['link_list'] = ['products/css/product.css']
        context['menu'] = ProductCategory.objects.all()
        context['product'] = self.get_object()

        return context


class ProductCreate(CreateView):
    model = Product
    success_url = reverse_lazy('products:main')
    form_class = ProductModelForm
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание продукта'
        context['link_list'] = ['server/css/crud.css']
        context['menu'] = ProductCategory.objects.all()

        return context


class ProductUpdate(UpdateView):
    model = Product
    success_url = reverse_lazy('products:main')
    form_class = ProductModelForm
    template_name = 'products/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение продукта'
        context['link_list'] = ['server/css/crud.css']
        context['menu'] = ProductCategory.objects.all()

        return context


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products:main')
    template_name = 'products/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление продукта'
        context['link_list'] = ['server/css/crud.css']
        context['menu'] = ProductCategory.objects.all()
        context['product'] = self.get_object()

        return context


def product_rest_list(request):
    object_list = Product.objects.all()
    data = []

    for itm in object_list:
        data.append(
            {
                'id': itm.id,
                'name': itm.name,
                'price_now': itm.price_now,
                'price_old': itm.price_old,
                'image_url': itm.image.url if itm.image else None,
                'status': itm.status
            }
        )

    return JsonResponse({'results': data})
