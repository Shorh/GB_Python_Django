from django.shortcuts import render


def start(request):
    return render(request, 'main/index.html')


def contacts(request):
    return render(request, 'main/contacts.html')
