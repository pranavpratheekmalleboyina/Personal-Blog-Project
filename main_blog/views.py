from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author":"Corey Anderson",
        "title":"My greatest memory",
        "content":"How I played an important part in MI qualifying in 2014",
        "date_posted":"27th May, 2014"
    },
    {
        "author":"Kane Willaimson",
        "title":"My worst memory",
        "content":"How a cricket rule robbed us of a world cup in 2019",
        "date_posted":"27th June, 2019"
    }
    
]
# Create your views here.
def home(request):
    context= {
        "posts":posts
    }
    return render(request,'main_blog/home.html',context)

def about(request):
    return render(request,'main_blog/about.html',{'title':'About section'})