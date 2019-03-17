from django.shortcuts import render


def main(request):
    return render(request, 'main/index.html')


def catalog(request):
    return render(request, 'main/catalog.html')


def karkasson(request):
    return render(request, 'main/catalog/karkasson.html')


def machi_koro(request):
    return render(request, 'main/catalog/machi-koro.html')


def manchkin(request):
    return render(request, 'main/catalog/manchkin.html')


def contact(request):
    return render(request, 'main/contacts.html')
