from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, UserChangeForm
)
from accounts.models import AccountUser


class LoginForm(AuthenticationForm):
    class Meta:
        model = AccountUser
        fields = ('username', 'password')


class CreationForm(UserCreationForm):
    class Meta:
        model = AccountUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'email',
            'phone',
            'avatar',
        )


class UpdateForm(UserChangeForm):
    class Meta:
        model = AccountUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'avatar',
            'password',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'password':
                field.widget = forms.HiddenInput
