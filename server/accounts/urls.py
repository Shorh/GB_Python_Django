from django.urls import path

from accounts.views import (
    AccountLogin, AccountLogout, AccountRegister, user_delete
)


app_name = 'accounts'

urlpatterns = [
    path('login/', AccountLogin.as_view(), name='login'),
    path('logout/', AccountLogout.as_view(), name='logout'),
    path('delete/', user_delete, name='delete'),
    path('register/', AccountRegister.as_view(), name='register'),
]
