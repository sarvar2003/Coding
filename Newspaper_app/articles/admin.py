from xml.etree.ElementTree import Comment
from django.contrib import admin

from .models import Article
from .models import Comment

admin.site.register(Article)
admin.site.register(Comment)
# Register your models here.
