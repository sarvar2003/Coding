from django.urls import path

from .views import ArticleListView, ArticleEditView, ArticleDeleteView, ArticleDetailView, ArticleCreateView

urlpatterns = [
    path('<int:pk>/edit/', ArticleEditView.as_view(), name = 'article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name = 'article_delete'),
    path('<int:pk>/detail/', ArticleDetailView.as_view(), name = 'article_detail'),
    path('new/', ArticleCreateView.as_view(), name = 'article_new'),
    path('', ArticleListView.as_view(), name = 'article_list'),
]