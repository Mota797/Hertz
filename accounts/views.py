from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import FormularioCriacaoUsuario

# Create your views here.
class Criacao_usuario(CreateView):
    model = User
    form_class = FormularioCriacaoUsuario
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False 
        user.save()

        messages.success(
            self.request,
            "Usuário registrado com sucesso !, você pode fazer login sem problemas."
        )

        return super().form_valid(form)