from django.urls import path
from main.views import (
    main, contacts
)


app_name = 'main'

urlpatterns = [
    path('', main, name='main'),
    path('contacts/', contacts, name='contacts'),
]
