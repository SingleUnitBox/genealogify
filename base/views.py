from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegForm
from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate

User = get_user_model()


def home(request):
    return render(request, 'main.html')

def register(request):
    form = UserRegForm()

    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            if User.objects.all().filter(email=request.POST.get('email')):
                messages.success(request, "ERROR")
            else:
                user = form.save()
                user.save()
                login(request, user)
                messages.success(request, "User successfully created..")
                return redirect('home')

    context = {'form': form}
    return render(request, 'login_register.html', context)

def user_login(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request, "User not found. Please register first.")
            return redirect('register')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}")
            return redirect('home')
        else:
            messages.warning(request, "Username or password does not exist.")
    context = {'page': page}
    return render(request, 'login_register.html', context)
