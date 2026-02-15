from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from decimal import Decimal
from django.db.models import Avg
from django.conf import settings


Usuario = settings.AUTH_USER_MODEL
class Produto(models.Model):

    CATEGORIAS_CHOICES = [
        ('fone_de_ouvido', 'Fone de Ouvido'),
        ('caixa_de_som', 'Caixa de Som'),
        ('microfone', 'Microfone'),
        ('mesa_de_Som_(mixer)', 'Mesa de Som (Mixer)')
    ]
    nome = models.CharField(max_length=200)
    preco = models.IntegerField()
    quantidade_estoque = models.IntegerField()
    categoria = models.CharField(max_length=200, choices=CATEGORIAS_CHOICES, blank=True)
    imagem = models.ImageField(default='padrao.png')
    imagem_carrossel_um = models.ImageField(default='padrao.png')
    imagem_carrossel_dois = models.ImageField(default='padrao.png')
 


    def preco_decimal(self):
        return Decimal(self.preco) / Decimal(100)

    def __str__(self):
        return f'{self.nome} - R$ {self.preco_decimal():.2f}'
    
    @property
    def preco_formatado(self):
        return f'{self.preco_decimal():.2f}'

    @property
    def media_avaliacoes(self):
        return self.avaliacao.aggregate( media=Avg('nota_avaliacao'))['media']

    @property    
    def quantidade_avaliacoes(self):
        return self.avaliacao.count()
    


class Avaliacao(models.Model):
    usuario = models.ForeignKey(Usuario,null=True, on_delete=models.CASCADE)
    nota_avaliacao = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
    comentario_avaliacao = models.TextField(blank=True)
    produto = models.ForeignKey(Produto, on_delete = models.CASCADE, related_name = 'avaliacao')

    def __str__(self):
        return f'{self.produto.nome} - Avaliação: {self.nota_avaliacao}'
