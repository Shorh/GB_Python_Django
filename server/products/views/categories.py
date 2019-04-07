from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView
)
from django.urls import reverse_lazy

from products.models import ProductCategory
from products.forms import CategoryModelForm


class CategoryList(ListView):
    model = ProductCategory
    template_name = 'categories/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории'
        context['link_list'] = ['']
        context['menu'] = ProductCategory.objects.all()
        context['obj'] = ProductCategory.objects.all()

        return context


class CategoryDetail(DetailView):
    model = ProductCategory
    template_name = 'categories/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_object().name
        context['link_list'] = ['products/css/product.css']
        context['menu'] = ProductCategory.objects.all()
        context['obj'] = self.get_object()

        return context


class CategoryCreate(CreateView):
    model = ProductCategory
    success_url = reverse_lazy('categories:main')
    form_class = CategoryModelForm
    template_name = 'categories/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание категории'
        context['link_list'] = ['server/css/crud.css']
        context['menu'] = ProductCategory.objects.all()

        return context


class CategoryUpdate(UpdateView):
    model = ProductCategory
    success_url = reverse_lazy('categories:main')
    form_class = CategoryModelForm
    template_name = 'categories/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение категории'
        context['link_list'] = ['server/css/crud.css']
        context['menu'] = ProductCategory.objects.all()

        return context


class CategoryDelete(DeleteView):
    model = ProductCategory
    success_url = reverse_lazy('categories:main')
    template_name = 'categories/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление категории'
        context['link_list'] = ['server/css/crud.css']
        context['menu'] = ProductCategory.objects.all()
        context['obj'] = self.get_object()

        return context
