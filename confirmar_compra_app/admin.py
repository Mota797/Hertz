from django.contrib import admin
from .models import Confirmacao_Compra, Item_Compra

# Register your models here.
@admin.register(Confirmacao_Compra)
class ConfirmacaCompraAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'metodo_pagamento','carrinho','data_compra',)

@admin.register(Item_Compra)
class ItemCompraAdmin(admin.ModelAdmin):
    list_display = ('compra','produto','quantidade_comprada','preco_unitario',)