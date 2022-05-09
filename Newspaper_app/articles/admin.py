from xml.etree.ElementTree import Comment
from django.contrib import admin

from .models import Article
from .models import Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 2

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)


