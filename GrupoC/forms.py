from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserEditForm(UserCreationForm):

    user = forms.CharField(label="Usuario")
    password1 = forms.CharField(label='Nueva Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir nueva contraseña', widget=forms.PasswordInput) 


    class Meta:
        model = User
        fields = [ 'user', 'password1', 'password2'] 
        


