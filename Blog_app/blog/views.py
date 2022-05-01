from tempfile import template
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Blog


class HomePageView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'all_blogs'
# Create your views here.
