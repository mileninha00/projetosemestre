from django import forms
from django.contrib.auth.models import User

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name':'Nome',
            'last_name': 'Sobrenome',
            'email':' E-mail',
        }