from hertz_app.models import Produto
from decimal import Decimal
from django.db import models
from django.conf import settings
from hertz_app.models import Usuario


class Carrinho_Compras(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    # itens = models.ManyToManyField(Produto, blank=True)
    # total = models.DecimalField(default = 0.00, max_digits=100, decimal_places=2)
    atualizado_em = models.DateTimeField(auto_now=True)
    guardado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def preco_total(self):
        preco_total_carrinho = Decimal(0.00)
        for i in self.itens.all():  
            preco_total_carrinho += i.total_por_produto
        
        return preco_total_carrinho
    
    
class Quantidade_Item_Carrinho(models.Model):
    carrinho = models.ForeignKey(
        Carrinho_Compras,
        related_name="itens",
        on_delete=models.CASCADE
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    @property
    def total_por_produto(self):
        return self.quantidade * self.produto.preco_decimal()