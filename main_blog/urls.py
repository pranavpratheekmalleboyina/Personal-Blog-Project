from django.urls import path,include
from django.contrib.auth import views as auth_views
from main_blog import admin
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('home/', views.home, name='main-blog-home'),
    path('about/', views.about, name='main-blog-about'),
]