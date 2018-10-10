from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the app index.")