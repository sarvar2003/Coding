from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text = 'asasa')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'asasa')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text = 'ususu')
    
    def test_proper_response(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_ulr_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    
    def test_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
# Create your tests here.
