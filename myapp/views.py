from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def user_menu(request):
    return render(request, 'user_menu.html')
