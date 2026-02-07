from django.test import TestCase
from carrinho_app.models import Carrinho_Compras, Quantidade_Item_Carrinho
from hertz_app.models import Produto
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.messages import get_messages

class TestViewCarrinho(TestCase):
    @classmethod
    def setUpClass(cls):
        Usuario = get_user_model()
        cls.usuario = Usuario.objects.create_user(
            username="Carlos",
            email="Carlos@email.com",
            password="uruguai"
        )

        cls.produto = Produto.objects.create(
            nome="microfone JBL",
            preco=5999,
            quantidade_estoque=1,
            categoria="microfone",
            imagem="padrao.png"
        )

        super(TestViewCarrinho, cls).setUpClass()

    def setUp(self):
        self.client.login(username="Carlos", password="uruguai")

        self.carrinho = Carrinho_Compras.objects.create(
            usuario=self.usuario
        )

        self.item_carrinho = Quantidade_Item_Carrinho.objects.create(
            carrinho=self.carrinho,
            produto=self.produto,
            quantidade=1
        )

    
    def test_redireciona_post_paginas_diversas(self):
        paginas = [
            '/',
            '/produto/1/'
        ]

        for pagina in paginas:
            response = self.client.post(reverse('adicionar_produto',args=[1]),HTTP_REFERER=pagina)
            self.assertRedirects(response, pagina)

    def test_redireciona_delete_carrinho(self):
        response = self.client.post(reverse('remover_produto',args=[1]),HTTP_REFERER='/carrinho/')
        self.assertRedirects(response, '/carrinho/')

    def test_remocao_acima_estoque(self):
        response = self.client.post(reverse('adicionar_produto', args=[1]),HTTP_REFERER='/')
        mensagens = list(get_messages(response.wsgi_request))

        self.assertTrue(any('limite em estoque.' in str(msg) for msg in mensagens))
