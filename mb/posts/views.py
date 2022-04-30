from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView

from posts.models import Post

class HomePage(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts_list'



# Create your views here.
