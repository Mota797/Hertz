from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Carrinho_Compras, Quantidade_Item_Carrinho
from hertz_app.models import Produto
from django.contrib import messages

class PaginaCarrinho(LoginRequiredMixin, TemplateView):
    template_name = 'carrinho.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        carrinho, criado = Carrinho_Compras.objects.get_or_create(
            usuario=self.request.user
        )

        context['carrinho'] = carrinho
        context['itens'] = carrinho.itens.all()
        context['total'] = carrinho.preco_total

        return context

    
class RemoverProdutoCarrinho(LoginRequiredMixin, View):

    def post(self, request, item_id):
        item = get_object_or_404(Quantidade_Item_Carrinho, id=item_id, carrinho__usuario=request.user)

        if item.quantidade > 1:
            item.quantidade -= 1
            item.save()
        else:
            item.delete()

        messages.info(request, "Produto removido do carrinho.")
        return redirect(request.META.get('HTTP_REFERER'))


class AdicionarProdutoCarrinho(LoginRequiredMixin, View):
    def post(self, request, item_id):
        produto = get_object_or_404(Produto, id=item_id)

        
        if produto.quantidade_estoque == 0:
            messages.error(request, "Produto sem estoque.")
            return redirect('carrinho')

        carrinho, criado = Carrinho_Compras.objects.get_or_create(
            usuario=request.user
        )

        item, criado = Quantidade_Item_Carrinho.objects.get_or_create(
            carrinho=carrinho,
            produto=produto,
            defaults={'quantidade': 1}
        )

        if not criado:
            if item.quantidade < produto.quantidade_estoque:
                item.quantidade += 1
            else:
                messages.warning(request, "A Quantidade do Item adicionado atingiu seu limite em estoque.")
                return redirect(request.META.get('HTTP_REFERER'))

        item.save()

        messages.success(request, "Produto adicionado ao carrinho.")
        return redirect(request.META.get('HTTP_REFERER'))

