from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords didn't match!! Please try again.")
            return render(request, 'register_page.html')

        else:
            user = User.objects.create_user(username=username, password=password1, email=email)
            messages.info(request, "Login with your credentials")
            return redirect('')

    else:
        return render(request, 'register_page.html')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            return render(request, 'homepage.html', context={'username': username})
        else:
            messages.error(request, "No user exists")
            return render(request, 'login_page.html')

    return render(request, 'login_page.html')








