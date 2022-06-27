from django.db import models


class Prato(models.Model):
    nome = models.CharField('Nome', max_length=255)
    descricao = models.TextField('Descrição')
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=18)
    imagem = models.ImageField('Imagem', blank=True)

    def __str__(self):
        return self.nome
