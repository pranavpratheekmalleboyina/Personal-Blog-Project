from django.urls import path
from main_blog import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
]