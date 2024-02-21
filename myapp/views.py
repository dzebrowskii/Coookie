from django.shortcuts import render
from django.http import JsonResponse
from recipes_management import recipes_management as rm

def index(request):
    return render(request, 'index.html')

def user_menu(request):
    return render(request, 'user_menu.html')

def guestapp(request):
    return render(request, 'guest_app.html')

def find_recipe(request):
    ingredients = request.GET.get('ingredients', '')
    results = rm.recipe_searcher(ingredients)
    return JsonResponse({'recipes': results})