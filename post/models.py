from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='imagens/%Y/%m/', blank=True, null=True)
    data_resposta = models.DateTimeField(auto_now_add=True)
    reacao = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.autor} - {self.data_resposta}'

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    legenda = models.TextField()
    imagem = models.ImageField(upload_to='imagens/%Y/%m/', blank=True, null=True)
    data_postagem = models.DateTimeField(auto_now_add=True)
    comentario = models.ManyToManyField(Comentario, null=True, blank=True)
    reacao = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.autor} - {self.data_postagem}'