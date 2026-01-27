from django.contrib import admin
from .models import Produto, Avaliacao
# Register your models here.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco_formatado', 'quantidade_estoque', 'categoria', 'imagem', 'media_avaliacoes', 'quantidade_avaliacoes')
    search_fields = ('nome',)
    list_filter = ('categoria', 'quantidade_estoque')



@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario','produto', 'nota_avaliacao', 'comentario_avaliacao',)
    search_fields = ('produto__nome',)
    list_filter = ('nota_avaliacao', 'usuario')