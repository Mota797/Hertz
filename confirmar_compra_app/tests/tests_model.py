from ..models import Confirmacao_Compra, Usuario, Carrinho_Compras, Item_Compra
from carrinho_app.models import Quantidade_Item_Carrinho, Produto
from django.test import TestCase

class ConfirmacaoCompraTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.usuario = Usuario.objects.create(username="Carlos",email="Carlos@email.com", first_name="Carlos", last_name="Silva")
        cls.carrinho = Carrinho_Compras.objects.create(usuario=cls.usuario)
        cls.produto = Produto.objects.create()
        cls.quantidade_item_carrinho = Quantidade_Item_Carrinho.objects.create(carrinho=cls.carrinho)

    def setUp(self):
        self.confirmacao_compra = Confirmacao_Compra.objects.create(
            usuario = self.usuario,
            metodo_pagamento = 'cartao_de_credito',
            carrinho = 1,

            )