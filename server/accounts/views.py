from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.views.generic import CreateView
from django.urls import reverse_lazy

from products.models import ProductCategory
from accounts.models import AccountUser
from accounts.forms import RegistrationForm


class AccountLogin(LoginView):
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        context['link_list'] = ['server/css/crud.css']
        context['menu'] = ProductCategory.objects.all()

        return context


class AccountLogout(LogoutView):
    next_page = reverse_lazy('main:main')


class AccountRegister(CreateView):
    model = AccountUser
    form_class = RegistrationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('main:main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['link_list'] = ['server/css/crud.css']
        context['menu'] = ProductCategory.objects.all()

        return context

    def post(self, *args, **kwargs):
        response = super().post(*args, **kwargs)
        login(self.request, self.object)

        return response


def user_delete(request):
    if request.method == 'POST':
        user = AccountUser.objects.get(id=request.user.id)
        user.delete()
        return redirect('main:main')

    return render(
        request,
        'accounts/delete.html',
        {
            'title': 'Удаление пользователя',
            'link_list': ['server/css/crud.css'],
            'menu': ProductCategory.objects.all(),
            'object': request.user,
        }
    )
