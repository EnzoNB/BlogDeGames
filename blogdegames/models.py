from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    título = models.CharField(max_length=255)
    tag_aba = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    corpo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.título + " | " + str(self.autor)
    
    def get_absolute_url(self):
        return reverse('article-detail',args=(str(self.id)))


    
