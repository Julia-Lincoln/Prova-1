from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse(request, 'todos')


# Create your views here.
