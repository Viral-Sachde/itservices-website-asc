from django.conf.urls import url, include
from django.contrib import admin
from django.urls import include, path
from . import views
from .views import feedback, savey

urlpatterns = [
               path('contact/', views.feedback, name='contact'),
               path('savey/', views.savey, name='savey'),
               path('savey2/', views.savey2, name='savey2'),
               path('services/', views.services, name='services'),
               path('home/', views.home, name='home'),
               path('portfolio/', views.portfolio, name='portfolio'),
          #     path('blog/', views.blog, name='blog'),
               path('tou/', views.tou, name='tou'),
               path('pp/', views.pp, name='pp'),
               ]
