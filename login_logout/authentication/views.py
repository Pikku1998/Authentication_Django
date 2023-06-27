from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def register(request):
    register_page = 'register_page.html'
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.error(request, "username already taken. please try with different username.")
            return render(request, register_page)
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered. Login using your credentials.")
            return render(request, register_page)
        if password1 != password2:
            messages.error(request, "Passwords didn't match!! Please try again.")
            return render(request, register_page)
        else:
            User.objects.create_user(username=username, password=password1, email=email)
            messages.info(request, "Login with your credentials")
            return redirect('sign_in')
    else:
        return render(request, register_page)


def sign_in(request):
    sign_in_page = 'login_page.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            request.session['username'] = username
            return redirect('home')
        else:
            messages.error(request, "No user exists")
            return render(request, sign_in_page)

    return render(request, sign_in_page)


@login_required(login_url='sign_in')
def home(request):
    homepage = 'homepage.html'
    username = request.session['username']
    return render(request, homepage, context={'username': username})


def sign_out(request):
    logout(request)
    return redirect('sign_in')









