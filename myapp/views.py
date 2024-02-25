from django.shortcuts import render, redirect
from django.http import JsonResponse
from recipes_management import recipes_management as rm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .forms import CreateUserForm, EmailChangeForm


def index(request):
    return render(request, 'index.html')


def user_menu(request):
    return render(request, 'user_menu.html')


def guestapp(request):
    return render(request, 'guest_app.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('logged_app')
        else:
            messages.info(request, 'Username or password is incorrect')

    constext = {}
    return render(request, 'login.html', constext)

@login_required(login_url='login')
def logged_app(request):
    return render(request, 'logged_app.html')


@login_required(login_url='login')
def logged_menu(request):
    return render(request, 'logged_menu.html')


def registration(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration.html', context)

@login_required(login_url='login')
def my_account(request):
    return render(request, 'my_account.html')

@login_required(login_url='login')
def password_change(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password changed successfully')
            return redirect('my_account')

    return render(request, 'password_change.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('login')

#
def find_recipe(request):
    ingredients = request.GET.get('ingredients', '')
    results = rm.recipe_searcher(ingredients)
    return JsonResponse({'recipes': results})


def email_change(request):
    if request.method == 'POST':
        form = EmailChangeForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data['new_email']
            confirm_email = form.cleaned_data['confirm_email']
            if new_email == confirm_email:
                request.user.email = new_email
                request.user.save()
                messages.success(request, 'Email changed successfully')
                return redirect('my_account')
            else:
                messages.info(request, 'Emails do not match')
                return redirect('email_change')
        else:
            messages.info(request, 'Invalid email')
            return redirect('email_change')

    return render(request, 'email_change.html', {'form': EmailChangeForm()})
