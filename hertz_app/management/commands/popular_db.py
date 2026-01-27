from django.core.management.base import BaseCommand
from hertz_app.models import Produto


class Command(BaseCommand):
    help = 'Insere produtos iniciais no banco de dados'

    def handle(self, *args, **options):
        produtos_dados = [
            {'nome':'Caixa de Som Bluetooth Boombox 3 JBL','preco':190000,'quantidade_estoque':80},
            {'nome':'Caixa de Som Bluetooth JBL Charge 6','preco':48000, 'quantidade_estoque':35},
            {'nome':'Caixa de Som Mancer Helmet, RGB, 2x3W RMS, USB, Preto, MCR-HMT-RGB01','preco':5199, 'quantidade_estoque':57},
            {'nome':'Headset Gamer TGT Diver V2, Rainbow, Drivers 40mm, Preto, TGT-DVR-RGB02','preco':4999, 'quantidade_estoque':16},
            {'nome':'Fone de Ouvido JBL Tune','preco':6490, 'quantidade_estoque':19}
        ]

        for item in produtos_dados:
            Produto.objects.get_or_create(**item)

        self.stdout.write(
            self.style.SUCCESS('Produtos inseridos com sucesso!')
        )
