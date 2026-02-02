from confirmar_compra_app.models import Confirmacao_Compra, Item_Compra
from carrinho_app.models import Quantidade_Item_Carrinho, Produto, Carrinho_Compras
from django.contrib.auth import get_user_model
from django.test import TestCase
from decimal import Decimal

class ConfirmacaoCompraTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        Usuario = get_user_model()
        cls.usuario = Usuario.objects.create(username="Carlos",email="Carlos@email.com", password='uruguai', first_name="Carlos", last_name="Silva")
        cls.produto = Produto.objects.create(nome='microfone JBL', preco=5999, quantidade_estoque=90, categoria='microfone', imagem='padrao.png')
        cls.carrinho = Carrinho_Compras.objects.create(usuario=cls.usuario)
        cls.quantidade_item_carrinho = Quantidade_Item_Carrinho.objects.create(carrinho=cls.carrinho, produto=cls.produto, quantidade=2)
        
    def setUp(self):
        self.confirmacao_compra = Confirmacao_Compra.objects.create(
            usuario = self.usuario,
            metodo_pagamento = 'cartao_de_credito',
            carrinho = self.carrinho,
            status = 'em_andamento'
            )
        
        self.item_compra = Item_Compra.objects.create(
            compra = self.confirmacao_compra,
            produto = self.produto,
            quantidade_comprada = 2,
            preco_unitario = self.produto.preco_decimal()
        )
        
    def test_compra_confirmada(self):
        self.assertEqual(self.usuario.username,'Carlos','O nome de usuário está incorreto')
        self.assertEqual(self.confirmacao_compra.metodo_pagamento,'cartao_de_credito','O método de pagamento está incorreto')
        self.assertEqual(self.carrinho.usuario.username,'Carlos','O nome de usuário do está incorreto')

    def test_item_compra(self):
        self.assertEqual(self.confirmacao_compra.usuario.username,'Carlos','O nome do usuário está incorreto')
        self.assertEqual(self.produto.nome,'microfone JBL','O produto está incorreto')
        self.assertEqual(self.item_compra.quantidade_comprada,2,'A quantidade comprada está incorreta')
        self.assertEqual(self.item_compra.preco_unitario, self.produto.preco_decimal(), 'O preco unitario está incorreto')
        self.assertEqual(self.item_compra.subtotal, Decimal("119.98"), 'O subtotal está incorreto')

