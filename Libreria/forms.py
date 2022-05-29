from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from Libreria.models import Avatar
class LectorFormulario(forms.Form):
    
    nombre= forms.CharField()
    apellido= forms.CharField()
    telefono= forms.IntegerField()
    libroEnPrestamo= forms.BooleanField(required= False)

class PrestamoFormulario(forms.Form):
    
    lector= forms.CharField()
    libro= forms.CharField()
    fechaDePrestamo= forms.DateField()
    devuelto= forms.BooleanField(required= False)

class LibroFormulario(forms.Form):
    
    nombre= forms.CharField()
    enPrestamo= forms.BooleanField(required= False)

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1: forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2: forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields= ['username', 'email', 'password1', 'password2']


class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['user', 'imagen']
        