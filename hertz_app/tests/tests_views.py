from django.test import TestCase
from hertz_app.models import Produto, Avaliacao
from django.contrib.auth import get_user_model
from decimal import Decimal

class TestViewsHertzApp(TestCase):
    @classmethod
    def setUpClass(cls):
        Usuario = get_user_model()
        cls.usuario = Usuario.objects.create_user(
            username="Carlos",
            email="Carlos@email.com",
            password="uruguai"
        )

        cls.produto = Produto.objects.create(
            nome='Microfone JBL', 
            preco=5999, 
            quantidade_estoque=90, 
            categoria='microfone', 
            imagem='padrao.png'
        )   
        super(TestViewsHertzApp, cls).setUpClass()

    def setUp(self):
        self.client.login(username="Carlos", password="uruguai")

        # self.avaliacao = Avaliacao.objects.create(
        #     usuario = self.usuario,
        #     nota_avaliacao = 5,
        #     comentario_avaliacao = 'Ótimo produto, utilizo todos os dias para gravar meu podcast Universo Escuro e ele não me deu problema uma única vez, além disso, a qualidade é impecável, recomendo muito, especiamente pra quem é criador de conteúdo.',
        #     produto = self.produto
        # )
    
    def test_view_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_detalhe_produto(self):
        response = self.client.get(f'/produto/{self.produto.pk}/')
        self.assertEqual(response.status_code, 200)