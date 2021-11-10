from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse('<h1>Homepage</h1><hr>E447B3A9B8C4')
