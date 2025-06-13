from django.urls import path,include
from django.contrib.auth import views as auth_views
from main_blog import admin
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('user/<str:username>',UserPostListView.as_view() ,name='user-posts'),
    path('post/<int:pk>', PostDetailView.as_view(),name='post-detail'),
    path('post/new', PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(),name='post-delete'),
    path('home/', PostListView.as_view(), name='main-blog-home'),
    path('about/', views.about, name='main-blog-about'),
]