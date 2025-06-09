from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required

# We create our views here
@login_required  #this is for the home page i.e. the one we return to where all the info is displayed
def home(request):
    context= {
        "posts": Post.objects.all()
    } 
    return render(request,'main_blog/home.html',context)

#This is the about section where a user can describe about themselves
@login_required
def about(request):
    return render(request,'main_blog/about.html',{'title':'About section'})