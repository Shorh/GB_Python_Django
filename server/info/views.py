from django.shortcuts import render


def start(request):
    return render(request, 'info/index.html')


def contact(request):
    return render(request, 'info/contacts.html')
