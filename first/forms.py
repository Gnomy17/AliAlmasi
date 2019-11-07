from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NameForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=False, help_text="first name")
    last_name = forms.CharField(max_length=100, required=False, help_text="last name")
    email = forms.EmailField(max_length=254, help_text="email")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

