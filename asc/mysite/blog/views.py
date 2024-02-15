from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import Article

from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'article_list.html', {'articles': articles})


def article_detail(request, slug):
    articles = Article.objects.get(slug=slug)
    return render(request, 'ad.html', {'articles': articles})

