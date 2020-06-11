from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Blog, BlogPost


class BlogsList(ListView):
    model = Blog


class BlogDetail(DetailView):
    model = Blog


class BlogPostDetail(DetailView):
    model = BlogPost
