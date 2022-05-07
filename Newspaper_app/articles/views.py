from django.urls import reverse_lazy

from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView

from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'all_articles'

class ArticleEditView(UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'body']

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ['title', 'body', 'author']

# Create your views here.
