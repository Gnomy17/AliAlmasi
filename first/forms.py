from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=False, help_text="first name")
    last_name = forms.CharField(max_length=100, required=False, help_text="last name")
    email = forms.EmailField(max_length=254, help_text="email")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)


class ContactForm(forms.Form):
    title = forms.CharField(required=True)
    text = forms.CharField(widget=forms.Textarea, required=True, max_length=250, min_length=10)
    email = forms.EmailField(required=True)
