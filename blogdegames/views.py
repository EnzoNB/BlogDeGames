from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, EditForm, CommentForm


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-data_postagem']


class ViewDetalhadaPost(DetailView):
    model = Post
    template_name = "article_details.html"


class ViewAdicionarPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"


class ViewAtualizarPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"


class ViewApagarPost(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')

class ViewAdicionarComentario(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"
    ordering = ['-comment_date']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
