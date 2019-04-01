from django.urls import path
from accounts.views import (
    login_view, logout_view, register_view, user_delete
)


app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('delete/', user_delete, name='delete'),
    path('register/', register_view, name='register'),
]
