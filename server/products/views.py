from django.shortcuts import render


def catalog(request):
    return render(request, 'products/index.html')


def karkasson(request):
    return render(request, 'products/karkasson.html')


def machi_koro(request):
    return render(request, 'products/machi-koro.html')


def manchkin(request):
    return render(request, 'products/manchkin.html')
