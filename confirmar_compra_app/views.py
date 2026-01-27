from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import Confirmacao_Compra, Item_Compra, Carrinho_Compras, Produto
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.contrib import messages

class ConfirmacaoCompra(LoginRequiredMixin, View):

    def post(self, request):
        with transaction.atomic():

            carrinho = self.get_carrinho(request)

            if not carrinho.itens.exists():
                messages.error(request, "Seu carrinho está vazio.")
                return redirect("ver_carrinho")

            compra = self.criar_compra(request, carrinho)

            self.criar_itens_e_atualizar_estoque(request, carrinho, compra)

            self.limpar_carrinho(carrinho)

            compra.status = "finalizada"
            compra.save()

            messages.success(request, "Compra realizada com sucesso!")
            return redirect("pagina_sucesso")

    # ==========================
    # MÉTODOS AUXILIARES
    # ==========================

    def get_carrinho(self, request):
        return get_object_or_404(Carrinho_Compras, usuario=request.user)

    def criar_compra(self, request, carrinho):
        return Confirmacao_Compra.objects.create(
            usuario=request.user,
            carrinho=carrinho,
            metodo_pagamento=request.POST.get("metodo_pagamento"),
            status="em_andamento"
        )

    def criar_itens_e_atualizar_estoque(self, request, carrinho, compra):
        for item in carrinho.itens.all():
            produto = item.produto

            # Verificação de estoque
            if item.quantidade > produto.estoque:
                messages.error(
                    request,
                    f"Estoque insuficiente para o produto {produto.nome}."
                )
                raise Exception("Estoque insuficiente")

            # Criar item da compra
            Item_Compra.objects.create(
                compra=compra,
                produto=produto,
                quantidade_comprada=item.quantidade,
                preco_unitario=produto.preco
            )

            # Atualizar estoque
            produto.estoque -= item.quantidade
            produto.save()

    def limpar_carrinho(self, carrinho):
        carrinho.itens.all().delete()

# class ConfirmacaoCompra(LoginRequiredMixin, View):
    
#     with transaction.atomic():
#         def post(self, request):
#            carrinho = self.get_carrinho(request)
#            compra = self.get_compra(request)
           
#            self.salvar_compra(carrinho, compra)
#            self.limpar_carrinho(carrinho)

#         def get_carrinho(request):
#             return get_object_or_404(Carrinho_Compras, carrinho__usuario=request.user)

#         def get_compra(request):
#             return get_object_or_404(Confirmacao_Compra, compra__usuario=request.user)

#         def salvar_compra(carrinho, compra):
#             itens_compra = []
#             compras_usuario = []
#             for produto in carrinho:
#                 item_compra = Item_Compra.objects.create(produto)
#                 itens_compra.append(item_compra)

#             for itens in itens_compra: 
#                 compra_usuario = compra.objects.create(itens)
#                 compras_usuario.append(compra_usuario)
            
#             return compras_usuario
        
#         def atualizar_estoque(compra):
#             for compra.itens in compra:
#                 if compra.itens.quantidade_comprada > Produto.quantidade_estoque:
#                     messages.error("Produto sem estoque.")
                
#                 else:
#                     Produto.quantidade_estoque -= compra.itens.quantidade_comprada



#         def limpar_carrinho(carrinho):
#             return carrinho.itens.all().delete()
    



