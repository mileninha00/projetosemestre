from django import forms
from .models import Movimentacao

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model=Movimentacao
        fields=['produto', 'quantidade', 'tipo']
        