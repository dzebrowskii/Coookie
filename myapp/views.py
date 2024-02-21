from django.shortcuts import render
from django.http import JsonResponse
from recipes_management import recipes_management as rm
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'index.html')


def user_menu(request):
    return render(request, 'user_menu.html')


def guestapp(request):
    return render(request, 'guest_app.html')


def login(request):
    return render(request, 'login.html')


def logged_app(request):
    return render(request, 'logged_app.html')


def logged_menu(request):
    return render(request, 'logged_menu.html')


def registration(request):
    form = UserCreationForm()
    context = {'form': form}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'registration.html', context)


def find_recipe(request):
    ingredients = request.GET.get('ingredients', '')
    results = rm.recipe_searcher(ingredients)
    return JsonResponse({'recipes': results})
