from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.urls import reverse
from post.models import Post, Comentario

class Feed(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()  # Adjust this query based on your model and filtering needs
        return render(request, 'feed.html', {'posts': posts})

class SalvarPost(View):
    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                'Você precisa fazer login.'
            )
            return redirect('perfil:cadastrar')

        legenda = self.request.POST.get('legenda')
        imagem = self.request.POST.get('imagem')
        data_postagem = self.request.POST.get('data_postagem')
        comentario = self.request.POST.get('comentario')
        reacao = self.request.POST.get('reacao')

        post = Post(
            autor=self.request.user,
            legenda=legenda,
            imagem=imagem,
            data_postagem=data_postagem,
            comentario=comentario,
            reacao=reacao
        )

        post.save()

        return redirect(
            reverse(
                'pedido:pagar',
                kwargs={
                    'pk': post.pk
                }
            )
        )

class SalvarComentario(View):
    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                'Você precisa fazer login.'
            )
            return redirect('perfil:cadastrar')

        texto = self.request.POST.get('texto')
        imagem = self.request.POST.get('imagem')
        data_resposta = self.request.POST.get('data_resposta')
        reacao = self.request.POST.get('reacao')

        comentario = Comentario(
            autor=self.request.user,
            texto=texto,
            imagem=imagem,
            data_resposta=data_resposta,
            reacao=reacao
        )

        comentario.save()

        return redirect(
            reverse(
                'pedido:pagar',
                kwargs={
                    'pk': comentario.pk
                }
            )
        )
