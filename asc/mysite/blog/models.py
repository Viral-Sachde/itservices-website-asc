from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    meta_des = models.CharField(max_length=500)
    meta_keywords = models.CharField(max_length=500)


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:250] + '...'
