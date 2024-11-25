from django.db import models
from produtos.models import Produto

class Movimentacao(models.Model):
    TIPO_MOVIMENTACAO = [
        ('E', 'Entrada'),
        ('S','Saida'),
    ]
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data= models.DateField(auto_now_add=True)
    tipo= models.CharField(max_length=1,choices= TIPO_MOVIMENTACAO)
    valor_total=models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.valor_total=self.produto.preco * self.quantidade 
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.produto.nome}-{self.quantidade} unidades em {self.data} - Total:R$ {self.valor_total}"