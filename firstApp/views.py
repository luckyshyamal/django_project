from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def firstapp(request):
    return HttpResponse("This is my first app")

def htmlfile(request):
    return render(request, 'index.html')

def htmlfile2(request):
    return render(request, 'index2.html')