from django.db import models
from hertz_app.models import Usuario, Produto
from carrinho_app.models import Carrinho_Compras


class Confirmacao_Compra(models.Model):
    METODOS_PAGAMENTO_CHOICES = [
        ('pix','PIX'),
        ('cartao_de_credito', 'Cartão de Crédito'),
        ('cartao_de_debito', 'Cartão de Débito')
    ]
    # STATUS_COMPRA_CHOICES = [
    #     ('em_andamento', 'Em Andamento'),
    #     ('finalizada', 'Finalizada'),
    #     ('cancelada', 'Cancelada')
    # ]
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='usuario_compras')
    metodo_pagamento = models.CharField(choices=METODOS_PAGAMENTO_CHOICES)
    carrinho = models.ForeignKey(Carrinho_Compras, on_delete=models.CASCADE) #SET_DEFAULT, default=)
    data_compra = models.DateTimeField(auto_now_add=True)
    # status = models.CharField(choices=STATUS_COMPRA_CHOICES)

class Item_Compra(models.Model):
    compra = models.ForeignKey(Confirmacao_Compra, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True)
    quantidade_comprada = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.quantidade_comprada * self.preco_unitario

