from django import forms
from .models import Avaliacao

class FormularioAvaliacao(forms.ModelForm):
    class Meta():
        model = Avaliacao
        fields = ('nota_avaliacao','comentario_avaliacao')
        widgets = {
            'nota_avaliacao': forms.HiddenInput(),
            'comentario_avaliacao': forms.Textarea(
                attrs={
                    'class': 'avaliacao-textarea',
                    'placeholder': 'Escreva suas impressões sobre o produto...',
                }
            )
        }