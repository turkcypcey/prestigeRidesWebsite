from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    return render( request, 'index.html')

def aboutUs(request):
    return render( request, 'aboutUs.html')

def brands(request):
    return render( request, 'brands.html')

def contactUs(request):
    return render( request, 'contactUs.html')