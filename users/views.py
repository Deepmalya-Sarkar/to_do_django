from django.shortcuts import render,redirect
from users.forms import (UserRegistrationForm,UserProfileForm,
                        UserProfileUpdateForm,UserUpdateForm)
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method=='POST':
        u_form=UserRegistrationForm(request.POST)
        p_form=UserProfileForm(request.POST,request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            u=User.objects.get(email=u_form.cleaned_data.get('email'))
            if u is None:
                user=u_form.save()
                user.save()
                profile=p_form.save(commit=False)
                profile.user=user
                if 'image' in request.FILES:
                    profile.image=request.FILES['image']
                profile.save()
                messages.success(request,"Your account has been created")
                return redirect('login')
            else:
                messages.error(request,"Email already present")
                return redirect('register')
    else:
        u_form=UserRegistrationForm()
        p_form=UserProfileForm()
    context={'u_form':u_form,'p_form':p_form}
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=UserProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,"Your profile has been updated")
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=UserProfileUpdateForm(instance=request.user.profile)
        context={'u_form':u_form,'p_form':p_form}
    return render(request,'users/profile.html',context)