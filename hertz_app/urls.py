from django.urls import path
from .views import home, detail_product

urlpatterns = [
    path('', home.as_view(), name = 'home'),
    path('produto/<int:pk>/', detail_product.as_view(), name = 'detalhe_produto'),
]