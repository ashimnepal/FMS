from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'body/main_index.html')


def About(request):
    return render(request, 'body/about.html')

def Enterprise(request):
    return render(request, 'body/enterprise.html')

def Pricing(request):
    return render(request, 'body/pricing.html')