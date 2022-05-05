from django.urls import path
from .views import (
    HomePageView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView
)

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'details'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name = 'delete_blog'),
    path('post/<int:pk>/edit/' , BlogUpdateView.as_view(), name = 'update_blog' ),
    path('post/new/', BlogCreateView.as_view(), name = 'new_blog'),
    path('', HomePageView.as_view(), name='home')
   
]