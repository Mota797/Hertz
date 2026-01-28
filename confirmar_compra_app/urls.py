from django.urls import path
from .views import ConfirmacaoCompra, PaginaSucesso, PaginaConfirmacaoCompra

urlpatterns = [
    path("", ConfirmacaoCompra.as_view(), name='confirmar_compra'),
    path("pagina_sucesso", PaginaSucesso.as_view(), name='pagina_sucesso'),
    path("pagina_confirmacao_compra", PaginaConfirmacaoCompra.as_view(), name='pagina_confirmacao_compra')           
    ]

