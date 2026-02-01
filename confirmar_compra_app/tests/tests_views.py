from django.test import TestCase
from confirmar_compra_app.models import Confirmacao_Compra, Item_Compra
from hertz_app.models import Produto
from carrinho_app.models import Carrinho_Compras, Quantidade_Item_Carrinho
from django.contrib.auth import get_user_model
from django.urls import reverse

class ViewConfirmarCompraTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Usuario = get_user_model()

        cls.usuario = Usuario.objects.create_user(
            username="Carlos",
            email="Carlos@email.com",
            password="uruguai"
        )

        cls.produto = Produto.objects.create(
            nome="microfone JBL",
            preco=5999,
            quantidade_estoque=90,
            categoria="microfone",
            imagem="padrao.png"
        )

    def setUp(self):
        self.client.login(username="Carlos", password="uruguai")

        self.carrinho = Carrinho_Compras.objects.create(
            usuario=self.usuario
        )

        self.item_carrinho = Quantidade_Item_Carrinho.objects.create(
            carrinho=self.carrinho,
            produto=self.produto,
            quantidade=2
        )

    def test_compra_salva_view(self):
        estoque_inicial = self.produto.quantidade_estoque

        response = self.client.post(
            reverse("confirmar_compra"),
            {
                "metodo_pagamento": "cartao_de_debito"
            }
        )

        # redirecionamento correto
        self.assertRedirects(response, reverse("pagina_sucesso"))

        # compra criada
        self.assertEqual(Confirmacao_Compra.objects.count(), 1)
        compra = Confirmacao_Compra.objects.first()

        self.assertEqual(compra.usuario, self.usuario)

        # item da compra criado
        self.assertEqual(Item_Compra.objects.count(), 1)
        item_compra = Item_Compra.objects.first()

        self.assertEqual(
            item_compra.quantidade_comprada,
            self.item_carrinho.quantidade
        )

        # estoque baixado corretamente
        self.produto.refresh_from_db()
        self.assertEqual(
            self.produto.quantidade_estoque,
            estoque_inicial - item_compra.quantidade_comprada
        )

        # carrinho limpo
        self.assertFalse(self.carrinho.itens.exists())
