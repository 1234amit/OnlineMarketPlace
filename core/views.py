from django.shortcuts import render, redirect
from items.models import Category, Item
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all() 
    return render(request, 'core/index.html', {'items':items, 'categories':categories})

def contact(request):
    return render(request, "core/contact.html")


def signUp(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully register! Welcome!")
            return redirect('/user_login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged in!")
            return redirect("index")
        else:
            messages.success(request, "There is a problem for login . Please Try again. ")
            return redirect("index")
    else:
        return render(request, 'core/login.html');

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("user_login")

