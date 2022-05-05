from django.urls import reverse_lazy
from dataclasses import fields
from pyexpat import model
from tempfile import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blog


class HomePageView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'all_blogs'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'detail.html'

class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog_form.html'
    fields = ['title', 'author', 'body']   

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'update_blog.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model =Blog
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')


# Create your views here.
