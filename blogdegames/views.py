from django.shortcuts import render, get_object_or_404, redirect 
from .models import Post 
from .forms import PostForm, EditForm  # Importando os forms PostForm e EditForm

def HomeView(request): 
    posts = Post.objects.all().order_by('-data_postagem')  # Obtendo todos os posts e ordenando por data de postagem
    return render(request, "home.html", {'posts': posts})  # Renderizando a página home.html com os posts

def ViewDetalhadaPost(request, pk):  
    post = get_object_or_404(Post, pk=pk)  # Obtendo o post pelo id, se não existir retorna 404
    return render(request, "article_details.html", {'post': post})  # Renderizando a página article_details.html com o post

def ViewAdicionarPost(request): 
    if request.method == "POST":  
        form = PostForm(request.POST)  # Cria um formulário com os dados do POST
        if form.is_valid():  # Se o formulário for válido
            form.save()  # Salva o post
        return redirect('/')  # Redireciona para a página inicial
    else:  
        form = PostForm()  # Cria um formulário vazio
    return render(request, "add_post.html", {'form': form})  # Renderiza a página add_post.html com o formulário

def ViewAtualizarPost(request, pk):  
    post = get_object_or_404(Post, pk=pk)  # Obtendo o post pelo id, se não existir retorna 404
    if request.method == "POST":  
        form = EditForm(request.POST, instance=post) 
        if form.is_valid(): 
            form.save()  
        return redirect('/')  
    else: 
        form = EditForm(instance=post) 
    return render(request, "update_post.html", {'form': form})  # Renderiza a página update_post.html com o formulário

def ViewApagarPost(request, pk):  
    post = get_object_or_404(Post, pk=pk)  
    if request.method == "POST": 
        post.delete()  # Deleta o post
        return redirect('/')  # Redireciona para a página inicial
    return render(request, "delete_post.html", {'post': post})  # Renderiza a página delete_post.html com o post
