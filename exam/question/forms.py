from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User, Question

class LoginForm(forms.Form):
    phone = forms.CharField(max_length=11, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

class CustomerUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['phone', 'password1', 'password2']


class CustomerUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['phone']


class SearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='Search Question!',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!'})
                  )