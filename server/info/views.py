from django.shortcuts import render


def start(request):
    return render(request, 'info/index.html')


def contacts(request):
    return render(request, 'info/contacts.html')
