from django.urls import path, include
from .views import HomeView, ViewDetalhadaPost, ViewAdicionarPost, ViewAtualizarPost, ViewApagarPost
urlpatterns = [
    path('',HomeView,name="home"),
    path('post/<int:pk>',ViewDetalhadaPost,name="article-detail"),
    path('posting/', ViewAdicionarPost, name = "add_post"),
    path('post/edit/<int:pk>', ViewAtualizarPost, name = "update_post"),
    path('post/delete/<int:pk>', ViewApagarPost, name = "delete_post"),
]
