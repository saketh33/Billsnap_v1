from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def ufff(request):
    return render(request, 'applist.html')
