from django import forms
from .models import User


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}
        )
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}
        )
    )


class UserRegistrationForm(forms.Form):
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}
        )
    )
    full_name = forms.CharField(
        label='Nombre completo',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre completo'}
        )
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Cree una contraseña'}
        )
    )


class ManagerLoginForm(forms.Form):
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}
        )
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}
        )
    )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email']
        labels = {
            'full_name': 'Nombre completo',
            'email': 'Correo electrónico',
        }