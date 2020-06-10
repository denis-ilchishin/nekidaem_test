from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Blog


class BlogsList(ListView):
    model = Blog


class BlogDetail(DetailView):
    model = Blog
