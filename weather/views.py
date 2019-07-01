from django.shortcuts import render
from django.http import HttpResponse

def map(request):
    return render(request, 'weather/map.html')

def list(request):
    return render(request, 'weather/list.html')

def search(request):
    return render(request, 'weather/search.html')

def alert(request):
    return render(request, 'weather/alert.html')

def index(request):
    return render(request, 'weather/index.html')