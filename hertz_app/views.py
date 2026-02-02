from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Produto
from django.contrib.auth.decorators import login_required

class home(ListView):
    model = Produto
    template_name = 'home.html'
    context_object_name = 'produtos'

class detail_product(DetailView):
    model = Produto
    template_name = 'detalhe_produto.html'

