from django.test import TestCase
from hertz_app.models import Produto, Avaliacao
from decimal import Decimal
from django.contrib.auth import get_user_model

class CriacaoProdutoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Usuario = get_user_model()
        cls.usuario = Usuario.objects.create(
            username="Carlos",email="Carlos@email.com", password='uruguai', first_name="Carlos", last_name="Silva"
        )

        cls.produto = Produto.objects.create(
            nome='Microfone JBL', 
            preco=5999, 
            quantidade_estoque=90, 
            categoria='microfone', 
            imagem='padrao.png'
        )
        
    def setUp(self):
        self.avaliacao = Avaliacao.objects.create(
            usuario = self.usuario,
            nota_avaliacao = 5,
            comentario_avaliacao = 'Ótimo produto, utilizo todos os dias para gravar meu podcast Universo Escuro e ele não me deu problema uma única vez, além disso, a qualidade é impecável, recomendo muito, especiamente pra quem é criador de conteúdo.',
            produto = self.produto
        )

    def test_produto_criado(self):
        self.assertEqual(self.produto.nome, 'Microfone JBL')
        self.assertEqual(self.produto.preco, 5999)
        self.assertEqual(self.produto.quantidade_estoque, 90)
        self.assertEqual(self.produto.categoria, 'microfone')
        self.assertEqual(self.produto.imagem, 'padrao.png')
        self.assertEqual(self.produto.preco_decimal(), Decimal('59.99'))
        self.assertEqual(self.produto.preco_formatado, '59.99')
        self.assertEqual(self.produto.quantidade_avaliacoes, 1)

    def test_produto_falso(self):
        self.assertNotEqual(self.produto.nome, 'Bola de futebol')
        self.assertNotEqual(self.produto.preco, 6000)
        self.assertNotEqual(self.produto.quantidade_estoque, 80)
        self.assertNotEqual(self.produto.categoria, 'fone_de_ouvido')
        self.assertNotEqual(self.produto.imagem, 'padraao.png')

    def test_avaliacao(self):
        self.assertEqual(self.avaliacao.usuario, self.usuario)
        self.assertEqual(self.avaliacao.nota_avaliacao, 5)
        self.assertEqual(self.avaliacao.comentario_avaliacao, 'Ótimo produto, utilizo todos os dias para gravar meu podcast Universo Escuro e ele não me deu problema uma única vez, além disso, a qualidade é impecável, recomendo muito, especiamente pra quem é criador de conteúdo.')
        self.assertEqual(self.avaliacao.produto, self.produto)
