from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EmailChangeForm(forms.Form):
    new_email = forms.EmailField(label='New Email')
    confirm_email = forms.EmailField(label='Confirm Email')
