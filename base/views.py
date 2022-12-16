from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegForm, MemberForm
from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate, logout
from .models import Member
User = get_user_model()


def home(request):
    return render(request, 'main.html')

def register(request):
    form = UserRegForm()

    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            if User.objects.all().filter(email=request.POST.get('email')):
                messages.warning(request, "ERROR")
            else:
                user = form.save()
                user.save()
                login(request, user)
                messages.success(request, "User successfully created.")
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

def user_logout(request):
    logout(request)
    return redirect('home')

def family(request):
    members = Member.objects.all()

    context = {'members': members}
    return render(request, 'family.html', context)

def add_member(request):
    form = MemberForm()
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = Member.objects.create(
                host=request.user,
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                nee_name=request.POST.get('nee_name'),
                place_of_birth=request.POST.get('place_of_birth'),
                place_of_death=request.POST.get('place_of_death'),
                date_of_birth=request.POST.get('date_of_birth'),
                date_of_death=request.POST.get('date_of_death'),
                date_of_marriage=request.POST.get('date_of_marriage'),
                notes=request.POST.get('notes'),
            )
            messages.success(request, f"Member {member} successfully added")
            return redirect('family')

    context = {'form': form}
    return render(request, 'add_edit.html', context)

def profile(request, pk):
    try:
        member = Member.objects.filter(id=pk)
    except:
        messages.warning(request, "Member not found.")

    context = {'member': member}
    return render(request, 'profile.html', context)

