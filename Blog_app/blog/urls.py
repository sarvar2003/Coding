from django.urls import path
from .views import HomePageView, BlogDetailView

urlpatterns = [
    path('blog/<int:pk>/', BlogDetailView.as_view(), name = 'details'),
    path('', HomePageView.as_view(), name='home')
   
]