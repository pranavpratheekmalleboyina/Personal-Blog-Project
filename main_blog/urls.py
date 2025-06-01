from django.urls import path
from main_blog import admin
from . import views

urlpatterns = [
    path('', views.home, name='main-blog-home'),
    path('about/', views.about, name='main-blog-about'),
]