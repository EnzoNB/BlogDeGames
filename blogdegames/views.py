from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post

def HomeView(request):
    posts = Post.objects.all().order_by('-data_postagem')     # Obtem todos os posts e ordena por data de postagem em ordem decrescente
    return render(request, "home.html", {'posts': posts})     # Renderiza a página home.html com os posts

def ViewDetalhadaPost(request, pk):
    post = get_object_or_404(Post, pk=pk)    # Obtem o post pelo id, se não existir retorna 404
    return render(request, "article_details.html", {'post': post})    # Renderiza a página article_details.html com o post

def ViewAdicionarPost(request):
    if request.method == "POST":    # Se o método for POST, cria um novo post
        post = Post()
        post.título = request.POST.get('titulo')
        post.autor = request.POST.get('autor')
        post.corpo = request.POST.get('corpo')
        post.save()
        return HttpResponseRedirect('/')    # Redireciona para a página inicial
    return render(request, "add_post.html" )    # Se o método for GET, renderiza a página add_post.html

def ViewAtualizarPost(request, pk):
    post = get_object_or_404(Post, pk=pk)    # Obtem o post pelo id, se não existir retorna 404
    if request.method == "POST":    # Se o método for POST, atualiza o post
        post.titulo = request.POST.get('titulo')
        post.autor = request.POST.get('autor')
        post.corpo = request.POST.get('corpo')
        post.save()
        return HttpResponseRedirect('/')    # Redireciona para a página inicial
    return render(request, "update_post.html", {'post': post})    # Se o método for GET, renderiza a página update_post.html com o post

def ViewApagarPost(request, pk):
    post = get_object_or_404(Post, pk=pk)    # Obtem o post pelo id, se não existir retorna 404
    if request.method == "POST":    # Se o método for POST, deleta o post
        post.delete()
        return HttpResponseRedirect('/')    # Redireciona para a página inicial
    return render(request, "delete_post.html", {'post': post})    # Se o método for GET, renderiza a página delete_post.html com o post

