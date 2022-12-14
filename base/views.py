from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegForm, MemberForm
from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate, logout
from .models import Member
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json

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
@login_required(login_url='login')
def family(request):
    q = request.GET.get('q')
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    lookups = Q(first_name__icontains=q) | Q(last_name__icontains=q)
    members = Member.objects.filter(lookups)

    paginator = Paginator(members, 50)
    page_number = request.GET.get('page')
    members = paginator.get_page(page_number)

    context = {'members': members}
    return render(request, 'family.html', context)
@login_required(login_url='login')
def add_member(request):
    page = 'add'
    form = MemberForm()
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save(commit=False)
            member.host = request.user
            member.save()
            # member = Member.objects.create(
            #     host=request.user,
            #     first_name=request.POST.get('first_name'),
            #     last_name=request.POST.get('last_name'),
            #     nee_name=request.POST.get('nee_name'),
            #     place_of_birth=request.POST.get('place_of_birth'),
            #     place_of_death=request.POST.get('place_of_death'),
            #     date_of_birth=request.POST.get('date_of_birth'),
            #     date_of_death=request.POST.get('date_of_death'),
            #     date_of_marriage=request.POST.get('date_of_marriage'),
            #     notes=request.POST.get('notes'),
            #     )
            # siblings_to_be_added = request.POST.getlist('siblings')
            # for sibling in siblings_to_be_added:
            #     member.siblings.add(sibling)
            # spouses_to_be_added = request.POST.getlist('spouses')
            # for spouse in spouses_to_be_added:
            #     member.spouses.add(spouse)
            # parents_to_be_added = request.POST.getlist('parents')
            # for parent in parents_to_be_added:
            #     member.parents.add(parent)
            messages.success(request, f"Member {member} successfully added")
            return redirect('family')

    context = {'form': form, 'page': page}
    return render(request, 'add_edit.html', context)
@login_required(login_url='login')
def edit_member(request, pk):
    member = Member.objects.get(id=pk)
    form = MemberForm(instance=member)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, f"Member {member} successfully edited")
        return redirect('family')
    context = {'form': form}
    return render(request, 'add_edit.html', context)
@login_required(login_url='login')
def delete_member(request, pk):
    try:
        member = Member.objects
    except:
        messages.warning(request, "Member not found.")
    else:
        if request.method == 'POST':
            member.delete()
            messages.success(request, f"Member successfully deleted.")
            return redirect('family')
@login_required(login_url='login')
def profile(request, pk):
    member = Member.objects.get(pk=pk)
    if member == None:
        messages.warning(request, "Member not found.")

    # member_data = serializers.serialize('json', member)
    # json_object = json.loads(member_data)[0]['fields']




    context = {'member': member}
    return render(request, 'profile.html', context)

