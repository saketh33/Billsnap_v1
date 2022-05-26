from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def sett_ings(request):
    return render(request, 'settings.html')

def dashboard(request):
    return render(request, 'dashboard.html')