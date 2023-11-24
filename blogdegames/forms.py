from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('título','tag_aba','autor','corpo')

        widgets = {
            'título': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Insira aqui o título de sua postagem"}),
            'tag_aba': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Insira aqui a tag de sua postagem"}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'corpo': forms.Textarea(attrs={'class': 'form-control',"placeholder":"Insira aqui de sua postagem"}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('título','tag_aba','corpo')

        widgets = {
            'título': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Insira aqui o título de sua postagem"}),
            'tag_aba': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Insira aqui a tag de sua postagem"}),
            'corpo': forms.Textarea(attrs={'class': 'form-control',"placeholder":"Insira aqui de sua postagem"}),
        }

