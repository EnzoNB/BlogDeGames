from django import forms
from .models import Post, Comment



class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('título','tag_aba','autor','Category','corpo')

        widgets = {
            'título': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Insira aqui o título de sua postagem"}),
            'tag_aba': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Insira aqui a tag de sua postagem"}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'corpo': forms.Textarea(attrs={'class': 'form-control',"placeholder":"Insira aqui de sua postagem"}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('título','tag_aba','Category','corpo')

        widgets = {
            'título': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Insira aqui o título de sua postagem"}),
            'tag_aba': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Insira aqui a tag de sua postagem"}),
            'corpo': forms.Textarea(attrs={'class': 'form-control',"placeholder":"Insira aqui de sua postagem"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('nome','corpo')

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Insira aqui o título de sua postagem"}),
            'corpo': forms.Textarea(attrs={'class': 'form-control',"placeholder":"Insira aqui de sua postagem"}),
        }