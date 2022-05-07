from tkinter import CASCADE
from turtle import title
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
# Create your models here.
