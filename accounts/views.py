from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

from django.contrib.auth import login, authenticate
from .forms import SignUpForm


'''
def signup(request):
    if request.method == 'POST':
        #the user has info and wants to create an account
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'User Exists'})
            except User.DoesNotExist:
                newuser = User.objects.create_user(request.POST['username'], request.POST['password1'])
                auth.login(request, newuser)
                return redirect("home")
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password must match'})
    else:
        # User wwants to enter an info
        return render(request, 'accounts/signup.html')
'''


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})



def loginUser(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
             return render(request, 'accounts/login.html', {'error': 'user name or password is incorrect. Please check your caps lock is not ON!'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect("home")
    # Route this to home page in near future and don't forget to log out.
    return render(request, 'accounts/signup.html')
