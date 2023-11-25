from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Posts
# Create your views here.


def home(request):
    datas = Posts.objects.all().order_by('-date')
    return render(request, 'blog/index.html', {'datas': datas})

def register_user(request):
    if request.method == 'POST':
        username= request.POST['username']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
            )
        user.save()
        return redirect('login_user')
    else:
        user = User()
    return render(request, 'blog/register_page.html', {'user': user})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')

        else:
            return render(request, 'login_page.html', {'error': 'Invalid credentials'})
    return render(request, 'blog/login_page.html')

def logout_user(request):
    logout(request)
    return render(request,'blog/logout_page.html')

def makepost(request):
    if request.method == 'POST':
        title = request.POST.get('postTitle')
        content = request.POST.get('postContent')
        posted = Posts.objects.create(
            title=title,
            content = content
        )
        posted.save()
        return redirect('home')

    return render(request, 'blog/makepost.html')


