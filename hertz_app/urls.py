from django.urls import path
from .views import home, detail_product, sobre_nos

urlpatterns = [
    path('', home.as_view(), name = 'home'),
    path('produto/<int:pk>/', detail_product.as_view(), name = 'detalhe_produto'),
    path('sobre_nos/', sobre_nos.as_view(), name = 'sobre_nos'),
]