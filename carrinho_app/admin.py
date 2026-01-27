from django.contrib import admin
from .models import Carrinho_Compras

@admin.register(Carrinho_Compras)
class Carrinho_Compras(admin.ModelAdmin):
    list_display = ('usuario','preco_total','atualizado_em','guardado_em')
    search_fields = ('usuario__username',)
    list_filter = ('usuario__username',)


    def listar_itens(self, obj):
            return ", ".join(
                item.nome for item in obj.itens.all()
            )

    listar_itens.short_description = 'Itens do carrinho'


