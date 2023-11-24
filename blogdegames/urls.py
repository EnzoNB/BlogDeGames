from django.urls import path, include
from .views import HomeView, ViewDetalhadaPost, ViewAdicionarPost, ViewAtualizarPost, ViewApagarPost

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('post/<int:pk>',ViewDetalhadaPost.as_view(),name="article-detail"),
    path('posting/', ViewAdicionarPost.as_view(), name = "add_post"),
    path('post/edit/<int:pk>', ViewAtualizarPost.as_view(), name = "update_post"),
    path('post/delete/<int:pk>', ViewApagarPost.as_view(), name = "delete_post"),
]
