from pyexpat import model
from tempfile import template
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog


class HomePageView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'all_blogs'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'detail.html'

# Create your views here.
