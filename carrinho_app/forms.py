from django import forms
from .models import Carrinho_Compras

class FormularioCarrinho(forms.ModelForm):
    class Meta():
        model = Carrinho_Compras
        fields = ('itens',)