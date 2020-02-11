from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpResponse


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    error_messages = {
        'duplicate_username': "Пользователь с таким именем уже существует",
        'password_mismatch': "Введенные пароли не совпадают",
    }

    field_order = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = 'Подсказка к логину'
        self.fields['password1'].help_text = 'Подсказка к паролю'
        self.fields['password2'].help_text = 'Подтверждение пароля'
