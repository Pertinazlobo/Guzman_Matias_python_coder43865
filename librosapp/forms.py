from django import forms
from .models import Libro, Cliente, Compra
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ("titulo", "autor", "precio")


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ("nombre", "apellido", "email")


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ("cliente", "libro", "fecha_compra")


class BusquedaLibrosForm(forms.Form):
    libro = forms.CharField(label="titulo", max_length=100)


class BusquedaComprasForm(forms.Form):
    busqueda = forms.CharField(max_length=100, required=False)


class BusquedaClienteForm(forms.Form):
    nombre_cliente = forms.CharField(label="Nombre del cliente", max_length=100)
    apellido_cliente = forms.CharField(label="Apellido del cliente", max_length=100)


class RegistroUsuariosForm(UserCreationForm):
    username = forms.CharField(max_length=20, label="Usuario")
    first_name = forms.CharField(label="nombre")
    last_name = forms.CharField(label="apellido")
    email = forms.EmailField(label="Email Usuario")
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmar contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
        help_texts = {A: "" for A in fields}


class UserEditForm(UserCreationForm):
    first_name = forms.CharField(label="nombre")
    last_name = forms.CharField(label="apellido")
    email = forms.EmailField(label="Email Usuario")
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmar contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
        help_texts = {k: "" for k in fields}


class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)
