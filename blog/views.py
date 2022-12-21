from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 6


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
