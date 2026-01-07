from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def gallery(request):
    return render(request, 'main/gallery.html')
