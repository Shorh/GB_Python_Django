from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import (
    authenticate, login, logout
)


from products.models import ProductCategory
from accounts.models import AccountUser
from accounts.forms import LoginForm, CreationForm, UpdateForm


def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(
                username=username,
                password=password,
            )

            if user and user.is_active:
                login(request, user)

                return redirect('main:main')

    return render(
        request,
        'accounts/login.html',
        {
            'title': '`Вход',
            'link_list': ['server/css/crud.css'],
            'menu': ProductCategory.objects.all(),
            'form': form,
        }
    )


def logout_view(request):
    logout(request)
    return redirect('main:main')


def register_view(request):
    form = CreationForm()
    if request.method == 'POST':
        form = CreationForm(
            data=request.POST,
            files=request.FILES,
        )
        if form.is_valid():
            form.save()
            return redirect('main:main')

    return render(
        request,
        'accounts/registration.html',
        {
            'title': 'Регистрация',
            'link_list': ['server/css/crud.css'],
            'menu': ProductCategory.objects.all(),
            'form': form,
        }
    )


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
            'name': request.user.username,
        }
    )
