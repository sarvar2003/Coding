from turtle import home, title
from urllib import response
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Blog

class BlogTests:
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@gmail.com',
            password = 'secret'
        )
        self.blog = Blog.objects.create(
            title = 'test_blog',
            body = 'Test body',
            author = self.user
        )

    def test_string_representation(self):
        blog = Blog(title='Sample Title')
        self.assertEqual(str(blog), blog.title)
    
    def test_blog_content(self):
        self.assertEqual(f'{self.blog.title}', 'test_blog')
        self.assertEqual(f'{self.blog.auhtor}', 'testuser')
        self.assertEqual(f'{self.blog.body}', 'Test body')

    def test_blog_list_view(self):
        response = self.client.get(reverse('home'))
        self.asserEqual(response.status_code, 200)
        self.assertContains(response, 'Test body')
        self.asserTemplateUsed(response, 'home.html')
    
    def test_blog_detail_view(self):
        response = self.client.get(reverse('/post/1'))
        no_response = self.client.get('/post/10000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assetContains(response, 'test_blog')
        self.assertTemplateUsed(response, 'detail.html')


