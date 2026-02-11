from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Produto
from django.contrib.auth.decorators import login_required
from django.db.models import Q

class home(ListView):
    model = Produto
    template_name = 'home.html'
    context_object_name = 'produtos'
    
    def get_queryset(self):
        query = self.request.GET.get('pesquisar')
        object_list = Produto.objects.all()

        if query:
            object_list = object_list.filter(Q(nome__icontains=query) | Q(categoria__icontains=query))
        
        return object_list

class detail_product(DetailView):
    model = Produto
    template_name = 'detalhe_produto.html'

