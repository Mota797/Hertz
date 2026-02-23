from django.contrib.auth.models import User
from django.contrib.auth import forms

class FormularioCriacaoUsuario(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = forms.UserCreationForm.Meta.fields 
        