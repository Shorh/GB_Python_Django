from django.urls import path
from .views import (
    catalog, karkasson, machi_koro, manchkin
)


urlpatterns = [
    path('karkasson/', karkasson, name='karkasson'),
    path('machi_koro/', machi_koro, name='machi_koro'),
    path('manchkin/', manchkin, name='manchkin'),
    path('', catalog, name='catalog'),
]
