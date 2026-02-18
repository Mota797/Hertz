from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Produto, Avaliacao
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import FormularioAvaliacao

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
    context_object_name = 'produto'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FormularioAvaliacao()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = FormularioAvaliacao(request.POST)

        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.usuario = request.user
            avaliacao.produto = self.object
            avaliacao.save()

            return redirect(reverse('detalhe_produto', kwargs={'pk': self.object.pk}))

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

    
        
class sobre_nos(TemplateView):
    template_name = 'sobre_nos.html'

