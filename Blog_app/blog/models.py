from tkinter import CASCADE
from turtle import title
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
       )
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
    
# Create your models here.
