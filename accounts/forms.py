from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CreateUserForm(forms.ModelForm):
    re_password = forms.CharField(
        label="re_assword",
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ('username', "first_name", "last_name", 'password',)

        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('parollar ikki xil iltimos 1 xil paroll berin ')
        return re_password

    # def save(self, commit=False):


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
