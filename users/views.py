from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def registerUser(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            username= form.cleaned_data.get('username')
            messages.success(request,'Account created successfully for {username}!')
            return redirect('main-blog-home')
    else:
        form = UserCreationForm()
    return render(request,"users/register.html",{'form':form})
    

