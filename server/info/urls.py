from django.urls import path
from .views import (
    start, contacts
)


urlpatterns = [
    path('', start, name='start'),
    path('contacts/', contacts, name='contacts'),
]
