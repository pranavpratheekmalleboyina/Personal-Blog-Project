from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm

# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f'Account created successfully! Please login ')
            return redirect('login')
        else:
            messages.error(request, 'There was a problem with your form. Please check the fields.')
    else:
        form = UserRegisterForm()
    return render(request,"users/register.html",{'form': form})

@login_required
def userProfile(request):
    if request.method == 'POST':
        userForm = UserUpdateForm(request.POST,instance=request.user)
        profileForm = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            messages.success(request,f'Your profile information has been updated!!')
            return redirect('profile')
    else:
        userForm = UserUpdateForm(instance=request.user)
        profileForm = ProfileUpdateForm(instance=request.user.profile)
                
    context={
        'userForm':userForm,
        'profileForm':profileForm
    }
    
    return render(request,"users/profile.html",context)
    

