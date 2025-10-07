from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def htmlfile(request):
    return render(request, 'index.html')

def htmlfile2(request):
    return render(request, 'index2.html')

def django_file(request):
    data2 = [1,2,3,4,5,6,7,8,9]
    data = {
        'Name': 'Shymal',
        'Age': 20,
        'City': 'Hyderabad',
        'numbers': data2
    }
    return render(request, 'django.html', data)