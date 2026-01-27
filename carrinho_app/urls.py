from django.urls import path
from .views import PaginaCarrinho, RemoverProdutoCarrinho, AdicionarProdutoCarrinho
urlpatterns = [ 
    path('', PaginaCarrinho.as_view() , name='carrinho'), 
    path('remover/produto/<int:item_id>', RemoverProdutoCarrinho.as_view() , name='remover_produto'),
    path('adicionar/produto/<int:item_id>', AdicionarProdutoCarrinho.as_view(), name='adicionar_produto')
    ]