from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, UserProfileForm, EditProfileForm


# Create your views here.


def home(request):

    return render(request,"authenticate/home.html",{})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, ('You have been Login  Successfully !'))
            return redirect('home')
            
        
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ('You have Fail to Login !'))
            return redirect('login')
        
    else:
           
        return render(request, 'authenticate/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have Been LogOut!'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            messages.success(request, ('You have Successfuly registered!'))
            login(request, user)
            return redirect('home')


    else:
        form = SignUpForm()
    context = {'form':form}     
    return render(request, 'authenticate/register.html', context)



def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()


            
            messages.success(request, ('You have Successfuly Edited Profile!'))
           
            return redirect('home')


    else:
        form = EditProfileForm(instance=request.user)
        profile_form= UserProfileForm()
    context = {'form':form, 'profile':profile_form}     
    
    return render(request, 'authenticate/edit_profile.html', context)


def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            update_session_auth_hash(request, form.user)


            
            messages.success(request, ('You have Successfuly Changed Password!'))
           
            return redirect('home')


    else:
        form = PasswordChangeForm(user=request.user)
        profile_form= UserProfileForm()
    context = {'form':form, 'profile':profile_form}     
    
    return render(request, 'authenticate/change_password.html', context)
    